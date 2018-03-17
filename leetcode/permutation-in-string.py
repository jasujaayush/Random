class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        h1 = collections.defaultdict(int)
        h2 = collections.defaultdict(int)
        n1= len(s1)
        
        for c in s1:
            h1[c]+=1
        
        for i,c in enumerate(s2):
            h2[c]+=1
            if i>= n1-1:
                if h2==h1:
                    return True
                else:
                    dc = s2[i-n1+1]
                    h2[dc] -= 1
                    if h2[dc]==0: del h2[dc]
        
        return False
        
