class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==2:
            return 1
        elif n==3:
            return 2
        else:
            p=1
            while n>4:
                p = p*3
                n -=3
            p *= n
            return p
