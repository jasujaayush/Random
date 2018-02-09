class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        results = {}
        stack = []
        for n in nums:
            while len(stack)>0 and stack[-1] < n:
                results[stack.pop()] = n
            stack.append(n)
        
        for i in range(len(findNums)):
            if results.has_key(findNums[i]):
                findNums[i] = results[findNums[i]]  
            else:
                findNums[i] = -1
        return findNums
