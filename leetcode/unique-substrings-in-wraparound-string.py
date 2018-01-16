class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        d = collections.defaultdict(int)
        mainstr = "abcdefghijklmnopqrstuvwxyza"
        p = "#"+p
        s = 0
        for i in range(1,len(p)):
            if p[i-1]+p[i] not in mainstr:
                s = i     
            d[p[i]] = max(d[p[i]], i-s+1)
            
        return sum(d.values())
