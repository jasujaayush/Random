class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        result = nums[0]
        maxSofar = nums[0]
        minSofar = nums[0]
        
        for x in nums[1:]:
            prevMax = maxSofar
            prevMin = minSofar
            maxSofar = max(x*prevMax, x*prevMin, x)
            minSofar = min(x*prevMax, x*prevMin, x)
            result = max(result, maxSofar)
        return result
