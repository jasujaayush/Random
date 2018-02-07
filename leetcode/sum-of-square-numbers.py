class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        i = 0
        while i*i <= c:
            b2 = c - i*i
            if int(b2**0.5) == b2**0.5:
                return True
            i += 1
        return False
