class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        sums = {}
        if nums[0] == 0:
            sums[0] = 2
        else:
            sums[nums[0]]  = 1
            sums[-nums[0]] = 1
            
        for n in nums[1:]:
            temp  = {}
            for k in sums.keys():
                temp[k+n] = temp.get(k+n,0) + sums[k]
                temp[k-n] = temp.get(k-n,0) + sums[k]
            sums = temp
        return sums.get(S,0)
        
        
        
        
