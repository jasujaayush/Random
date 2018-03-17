class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def bsearch(array, val, s, e):
            if s>e:
                return -1
            
            m = (s+e)/2
            if array[m] == val:
                return m
            elif array[m] > val:
                return bsearch(array, val, s, m-1)
            else:
                return bsearch(array, val, m+1, e)
        
        count = 0
        nums.sort()
        prev = None
        for i,n in enumerate(nums):
            index = bsearch(nums, n+k, i+1, len(nums)-1)
            #print prev, n, n+k, index
            if prev != n and index >= 0:
                count += 1
                prev = n
        return count
