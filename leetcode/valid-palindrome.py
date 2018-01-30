class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = "".join([c.lower() for c in s if c.isalnum()])
        n = len(s)
        for x in range(n/2):
            if s[x] != s[n-x-1]:
                return False
        return True
        
