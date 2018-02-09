class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        stack = []
        length = len(nums)
        results = [-1]*length
        for i in range(length)*2:
            while len(stack) and nums[stack[-1]] < nums[i]:
                results[stack.pop()] = nums[i]
            stack.append(i)
        return results
            
        
