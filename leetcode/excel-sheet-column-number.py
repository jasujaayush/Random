class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        col = 0
        for i,c in enumerate(s):
            col = col*26 + (ord(c) - ord('A') + 1)
        return col
