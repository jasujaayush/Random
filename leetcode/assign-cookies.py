class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        i = 0
        
        for c in s:
            if g[i] <= c: i+=1
            if i==len(g): break
        
        return i
        
