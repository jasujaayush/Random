"""Downloads YouTube8M Dataset files for a specific partition from a mirror.

This download script will be served from http://data.yt8m.org/download.py. The
partitions are 1/{frame_level,video_level}/{train,validate,test}

To run locally, do:
  cat download.py | partition=1/video_level/train mirror=us python

Or to download just 1/1000th of the data:
  cat download.py | shard=1,1000 partition=1/video_level/train mirror=us python
"""

import hashlib
import json
import os
import sys
import numpy as np
import tensorflow as tf

def hasRelevantLabels(labels):
	for l in labels:
		if int(l) in [1,4,40,47]:
			return True


def md5sum(filename):
  """Computes the MD5 Hash for the contents of `filename`."""
  md5 = hashlib.md5()
  with open(filename, 'rb') as fin:
    for chunk in iter(lambda: fin.read(128 * md5.block_size), b''):
      md5.update(chunk)
  return md5.hexdigest()


if __name__ == '__main__':
  if 'partition' not in os.environ:
    print >> sys.stderr, (
        'Must provide environment variable "partition". e.g. '
        '0/video_level/train')
    exit(1)
  if 'mirror' not in os.environ:
    print >> sys.stderr, (
        'Must provide environment variable "mirror". e.g. "us"')
    exit(1)

  partition = os.environ['partition']
  mirror = os.environ['mirror']
  partition_parts = partition.split('/')

  assert mirror in {'us', 'eu', 'asia'}
  assert len(partition_parts) == 3
  assert partition_parts[1] in {'video_level', 'frame_level'}
  assert partition_parts[2] in {'train', 'test', 'validate'}

  plan_url = 'http://data.yt8m.org/{}/download_plans/{}_{}.json'.format(
      partition_parts[0], partition_parts[1], partition_parts[2])

  num_shards = 1
  shard_id = 1
  if 'shard' in os.environ:
    if ',' not in os.environ['shard']:
      print ('Optional environment variable "shards" must be "X,Y" if set, '
             'where the integer X, Y are used for sharding. The files will be '
             'deterministically sharded Y-way and the X-th shard will be '
             'downloaded. It must be 1 <= X <= Y')
      exit(1)

    shard_id, num_shards = os.environ['shard'].split(',')
    shard_id = int(shard_id)
    num_shards = int(num_shards)
    assert shard_id >= 1
    assert shard_id <= num_shards

  if os.system('which curl') != 0:
    print >> sys.stderr, 'Error: curl is not installed. Install it and re-try'

  plan_filename = '%s_download_plan.json' % partition.replace('/', '_')

  if os.path.exists(plan_filename):
    print ('Resuming Download ...')
  else:
    print ('Starting fresh download in this directory. Please make sure you '
           'have >2TB of free disk space!')
    os.system('curl %s > %s' % (plan_url, plan_filename))

  download_plan = json.loads(open(plan_filename).read())

  files = [f for f in download_plan['files'].keys()
           if int(hashlib.md5(f).hexdigest(), 16) % num_shards == shard_id - 1]

  print ('Files remaining %i' % len(files))
  for f in files:
    print ('Downloading: %s' % f)

    #################### condition check
    with open('videos.txt', 'r') as myfile:
    	links = myfile.read().replace('\n', '')
    if f in links:
      print ('Skipping already downloaded file %s' % f)
      continue	
    ####################  

    if os.path.exists(f) and md5sum(f) == download_plan['files'][f]:
      print ('Skipping already downloaded file %s' % f)
      continue

    download_url = 'http://%s.data.yt8m.org/%s/%s' % (mirror, partition, f)
    os.system('curl %s > %s' % (download_url, f))
    if md5sum(f) == download_plan['files'][f]:
      print ('Successfully downloaded %s\n\n' % f)

      ########### My Code ###############

	  record_iterator = tf.python_io.tf_record_iterator(path=f)
	  for string_record in record_iterator:
		example = tf.train.Example()
		example.ParseFromString(string_record)
		x = str(example.features.feature['video_id'].bytes_list)
		vid = x.strip().split('"')[1]
		l = str(example.features.feature['labels'].int64_list)
		labels = l.replace('value:','').strip('\n').split()
		if hasRelevantLabels(labels):
			#write the videl link in file
			url = 'https://www.youtube.com/watch?v=' + vid + '\n'
			fi = open('videos.txt','aw')
			string = f + " :" + str(labels) + " : " + url
			fi.write(string)
			fi.close()
			
		#delete the record
		os.system('rm ' + f)

      ###########

      del download_plan['files'][f]
      open(plan_filename, 'w').write(json.dumps(download_plan))
    else:
      print ('Error downloading %s. MD5 does not match!\n\n' % f)

  print ('All done. No more files to download.')
