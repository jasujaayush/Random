class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import defaultdict
        d = defaultdict(int)
        for c in s:
            d[c] += 1
        
        r = ''
        for count, char in sorted(d.iteritems(), key=lambda (x,y):(y,x), reverse=True):
            r += char*count
        return r
        
