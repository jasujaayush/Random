class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        def issubsequence(s1, s2):
            i = 0
            for c in s2:
                if s1[i] == c: i+=1
                if i==len(s1): return True
                 
            return False
            
        
        def f(x,y):
            return 1 if len(x) >= len(y) else -1
        strs.sort(cmp=f, reverse=True)
        
        for i, s1 in enumerate(strs):
            res = True
            for j, s2 in enumerate(strs):
                if j != i:
                    res = res and (not issubsequence(s1, s2))
                    if not res: break
            if res:
                return len(s1)
        
        return -1
