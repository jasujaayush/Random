class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = max(nums)
        second = None
        for n in nums:
            if (second == None or n>second) and n<first:
                second = n
                
        third = None
        for n in nums:
            if (third == None or n>third) and second != None and n<second:
                third = n
                
        if third == None: third = first
        
        return third
