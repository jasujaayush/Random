class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        from collections import defaultdict
        count = defaultdict(int)
        currentSum = 0
        idealSum = len(nums)*(len(nums)+1)/2
        duplicate = 0
        for n in nums:
            currentSum += n
            count[n] += 1
            if count[n] > 1:
                duplicate = n
        return [duplicate, idealSum-currentSum+duplicate]
        
