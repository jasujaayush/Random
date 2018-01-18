class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        
        maxSoFar = [0]*len(nums)
        for i in range(len(nums)):
            if i==0:
                maxSoFar[i] = nums[i]
            elif i==1:
                maxSoFar[i] = max(nums[i], nums[i-1])
            else:
                maxSoFar[i] = max(nums[i] + maxSoFar[i-2], maxSoFar[i-1])
        return maxSoFar[len(nums)-1]
                
