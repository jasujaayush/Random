class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
            
        
        maxima = max(nums)
        minima = min(nums)
        N = len(nums)
        avgGap = math.ceil(float(maxima - minima)/(N-1))
        
        minBucket = [1000000000000000]*(N-1)
        maxBucket = [-100000000000000]*(N-1)
        
        for n in nums:
            if n != minima and n !=maxima:
                bucket = int((n - minima)/avgGap)
                minBucket[bucket] =  min(minBucket[bucket], n)
                maxBucket[bucket] =  max(maxBucket[bucket], n)
                
        maxGap = avgGap
        prevMax = minima
        for i in range(N-1):
            if maxBucket[i] != -100000000000000 and minBucket[i] != 1000000000000000:
                maxGap = max(minBucket[i]-prevMax, maxGap)
                prevMax = maxBucket[i]
        
        maxGap = max(maxima-prevMax, maxGap)
        return int(maxGap)
