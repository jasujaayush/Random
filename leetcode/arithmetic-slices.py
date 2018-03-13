class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        total = 0
        count = 0
        diff = None
        for i in range(2, len(A)):
            if diff != None and A[i] - A[i-1] == diff:
                count += 1
            elif A[i] - A[i-1] == A[i-1] - A[i-2]:
                diff = A[i] - A[i-1]
                count = 3
            elif count:
                total += ((count-1)*(count-2))/2
                count = 0
                diff = None
                
        if count:
            total += ((count-1)*(count-2))/2
                
        return total
