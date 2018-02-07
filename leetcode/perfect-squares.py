class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = [0]
        for num in range(1,n+1):
            minima = 100000000000000
            i = 1
            while i*i <= num:
                minima = min(minima, 1 + count[num-i*i])
                i += 1
            count.append(minima)
        return count[-1]
            
            
        
        
        
        
