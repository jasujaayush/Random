class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if len(nums) <= 2:
            return "/".join([str(n) for n in nums])
        return str(nums[0])+'/(' + "/".join([str(n) for n in nums[1:]]) +')'
