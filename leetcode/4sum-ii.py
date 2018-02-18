class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        from collections import defaultdict
        absum = defaultdict(int)
        cdsum = defaultdict(int)
        
        for a in A:
            for b in B:
                absum[a+b] += 1
        
        count = 0
        for c in C:
            for d in D:
                count += absum[-c-d]
        return count
        
        
        
        
