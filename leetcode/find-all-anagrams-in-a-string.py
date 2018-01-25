class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(p) > len(s):
            return []
        
        from collections import defaultdict
        pmap = defaultdict(int)
        newMap = defaultdict(int)
        results = []
        
        for c in p:
            pmap[c] += 1
        substr = ''
        for i in range(len(s)):
            c = s[i]
            newMap[c] += 1
            substr += c
            if len(substr) == len(p):
                findex = i - len(p) + 1
                if newMap == pmap: 
                    results.append(findex)
                newMap[s[findex]] -= 1
                if newMap[s[findex]] == 0: del newMap[s[findex]]
                substr = substr[1:]
            
        
            
        return results
