class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sets = [[]]
        for n in nums:
            newSets = []
            for s in sets:
                ns = s + [n]
                newSets.append(ns)
            sets = sets + newSets
        return sets
        
        
