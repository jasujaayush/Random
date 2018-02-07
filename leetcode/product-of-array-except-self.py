class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [1 for _ in range(len(nums))]
        
        prod = 1 #Forward Pass
        for i in range(len(nums)-1):
            prod *= nums[i] 
            result[i+1] *= prod
            
        prod = 1 #Backward Pass
        for i in range(len(nums)-1,0,-1):
            prod *= nums[i] 
            result[i-1] *= prod
        
        return result
        
