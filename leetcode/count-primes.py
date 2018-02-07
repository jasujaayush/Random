class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = range(0,n)
        i=2
        while i <= len(nums)**0.5:
            if nums[i] != 0:
                k = 2*i
                while k < len(nums):
                    if k%i == 0:
                        nums[k] = 0
                    k += i
            i += 1
            
        count = 0
        for n in nums[2:]:
            if n != 0:
                count+=1
        return count
                
            
            
        
        
