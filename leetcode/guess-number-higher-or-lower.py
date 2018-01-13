# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        m = n
        while True:
            g = (l+m)/2
            r = guess(g)
            #print l,m,g,r
            if r == 0:
                return g
            elif r == 1:
                l = g+1
            else:
                m = g-1
