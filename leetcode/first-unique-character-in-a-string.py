class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import defaultdict
        d = defaultdict(int)
        for c in s:
            d[c] += 1
            
        candidate = []
        for k in d:
            if d[k] == 1:
                candidate.append(k)
                
        for i,c in enumerate(s):
            if c in candidate:
                return i
        return -1
        
