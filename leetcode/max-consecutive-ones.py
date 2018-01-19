class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_count = 0
        current_count = 0
        for n in nums:
            if n==0:
                max_count = max(max_count, current_count)
                current_count = 0
            if n==1:
                current_count += 1
        max_count = max(max_count, current_count)
        return max_count
