class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        median = []
        window = nums[:k-1]
        for i in range(k-1, len(nums)):
            bisect.insort(window, nums[i])
            window.sort()   
            #print window, window[k/2], window[-k/2]
            m = (window[k/2] + window[(k-1)/2])/float(2)
            median.append(m)
            del window[window.index(nums[i-k+1])]
        return median
