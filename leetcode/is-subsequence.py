class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        j = 0
        for i, c in enumerate(s):
            while j<len(t) and t[j] != c:
                j += 1
            if j==len(t):
                return False
            else:
                j += 1
        return True
        
