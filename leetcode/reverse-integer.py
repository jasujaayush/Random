class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1 - 2*int(x<0)
        r = sign*int(str(abs(x))[::-1])
        if abs(r) >= 2**31-1: r = 0
        return r
