class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for i in range(33):
           if n&(2**i)>0:
            count += 1
        return count
