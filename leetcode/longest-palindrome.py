class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars = {}
        for c in s:
            if chars.has_key(c):
                chars[c] += 1
            else:
                chars[c] = 1
        
        flag = 0
        count = 0
        for c in chars:
            if chars[c]%2 == 0:
                count += chars[c]
            else:
                flag = 1
                count += (chars[c]/2)*2
        
        if flag == 1:
            count += 1
                
        return count
