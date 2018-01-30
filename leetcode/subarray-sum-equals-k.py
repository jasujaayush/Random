class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import defaultdict
        count = defaultdict(int)
        count[0] = 1
        psum = 0
        sumCountK = 0
        for x in nums:
            psum += x
            sumCountK += count[psum-k]
            count[psum] += 1
            
        return sumCountK
                
                
            
