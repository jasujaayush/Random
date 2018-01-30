class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        for x in range(n/2):
            if s[x] != s[n-x-1]:
                return False
        return True
    
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        for x in range(n/2):
            if s[x] != s[n-x-1]:
                return self.isPalindrome(s[x+1:n-x]) or self.isPalindrome(s[x:n-x-1]) #one of these has to be a palindrome
        return True
        
