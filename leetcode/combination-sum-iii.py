class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def helper(k,total, nums, results):
            if k==0 and total==0:
                results.append(nums[1:])
            
            for i in range(nums[-1]+1,10):
                if k>0 and i<=total:
                    nums.append(i)
                    helper(k-1, total-i, nums, results)
                    nums.pop()
        results = []
        helper(k, n, [0], results)
        return results
                
        
        
