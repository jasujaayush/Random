class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            x = nums[i]
            while x > 0 and x<len(nums) and nums[x-1] != x:
                t = nums[x-1]
                nums[x-1] = x
                nums[i] = x = t
                #print nums
                        
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        return len(nums)+1
        
