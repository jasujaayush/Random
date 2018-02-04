class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import defaultdict
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        
        return [key for key, value in sorted(count.iteritems(), key=lambda (n, value):(value,n), reverse=True)[:k]]
