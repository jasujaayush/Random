class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen = set()
        P = [] 
        v = 0
        for x in nums:
            v += x
            if k: v %= abs(k)
                
            if k==0 and v==0 and len(P)>0 and P[-1] == 0:
                return True
            elif k != 0 and ((len(P)>0 and v==0) or (v in seen)):
                return True
            P.append(v)
            seen.add(v)
        return False
