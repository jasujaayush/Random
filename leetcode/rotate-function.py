class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        asum = sum(A)
        f0 = 0
        for i,n in enumerate(A):
            f0 += i*n
        maxSofar = f0
        fkminus1 = f0
        for k in range(1,len(A)):
            fk = fkminus1 + len(A)*A[k-1] - asum
            maxSofar = max(maxSofar, fk)
            fkminus1 = fk
        return maxSofar
