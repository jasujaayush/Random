class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        results = [[] for _ in range(len(nums))]
        nums.sort(reverse = True)
        overall_best = []
        for i,num in enumerate(nums):
            best = [num]
            maxima = len(best)
            for j in range(i):
                if nums[j]%num == 0 and len(best) < len(results[j]) + 1:
                    best = [num] + results[j]
            results[i] = best
            if len(best) > len(overall_best):
                overall_best = best
            
        return overall_best
        
