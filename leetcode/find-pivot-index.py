class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sumnums = sum(nums)
        left = 0
        
        for i in range(len(nums)):
            n = nums[i]
            if left == sumnums - left - n:
                return i
            left += n
        return -1
