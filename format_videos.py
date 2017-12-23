import glob
import sys
import subprocess as sp
        
        
class ConvertPipe:
    def __init__(self, INPUTFOLDER, OUTPUTFOLDER):
        self.OUTPUTFOLDER = OUTPUTFOLDER
        self.INPUTFOLDER = INPUTFOLDER
        
    def process(self):
        sys.stdout.write("starting conversion...\n")
        filenames = glob.glob(self.INPUTFOLDER + "*/*")
        labels = set([f.split("/")[-2] for f in filenames])
        labels_count = dict(zip(list(labels), [0 for i in range(len(labels))]))
        for lab in labels:
            cmd = "mkdir " + self.OUTPUTFOLDER + lab
            sp.call(cmd,shell=True)
        for f in filenames:
            sys.stdout.write("converting "+f+"...\n")
            l = f.split("/")[-2]
            c = labels_count[l]
            self.convertVideo(f, c)
            labels_count[l]+=1
        sys.stdout.write("completed!\n")
            
        
    def convertVideo(self, filename, c):
        label = filename.split("/")[-2]
        filename = filename.replace(" ", "\ ").replace("(", "\(").replace(")", "\)")
        cmd1 = "mkdir " + self.OUTPUTFOLDER + label + "/" + str(c)
        print "################" + cmd1
        sp.call(cmd1,shell=True)
        outputpath= self.OUTPUTFOLDER + label + "/" + str(c) + "/"
        
        outputfile = outputpath + "f"
        cmd2='ffmpeg -i '+filename+' -vframes 500 -r 5 -s 224x224 ' + outputfile + '_%04d.jpg'
        sp.call(cmd2,shell=True)
        sys.stdout.write("Saved it at " + outputfile +"\n")



if __name__ == "__main__":
    import sys
    args = sys.argv
    inpt = args[1]
    outp = args[2]
    print args
    c = ConvertPipe(inpt, outp)
    c.process()
