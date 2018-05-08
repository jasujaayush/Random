class Solution(object):
    def helper(self, nums):
        if len(nums) == 1:
            return nums[0]
    
        m = len(nums)/2
        if nums[m-1] == nums[m]:
            if m%2==1:
                nums = nums[m+1:]
                return self.helper(nums)
            else:
                nums = nums[:m-1]
                return self.helper(nums)
        elif nums[m] == nums[m+1]:
            if m%2==0:
                nums = nums[m+2:]
                return self.helper(nums)
            else:
                nums = nums[:m]
                return self.helper(nums)
        else:
            return nums[m]
        
    
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.helper(nums)
        
        
