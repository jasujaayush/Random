class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        from collections import defaultdict
        count = defaultdict(int)
        
        for word in words:
            count[word] += 1
        wordCounts = [(key, value) for key, value in sorted(count.iteritems(), key=lambda (w,c): (c,w))]
        
        countToWords = defaultdict(list)
        for key,value in wordCounts:
            countToWords[value] += [key]
            
        results = []
        for key, value in sorted(countToWords.iteritems(), key=lambda (c,words): (c,words), reverse = True):
            value.sort()
            results += value[:k-len(results)]
            if len(results) == k:
                break
        return results
            
        
        
