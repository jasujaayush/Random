class Solution(object):
    def helper(self, cost, i, dp):
        if i >= len(cost):
            return 0
        
        if dp.has_key(i):
            return dp[i]
        else:
            dp[i] = temp = cost[i] + min(self.helper(cost, i+1, dp), self.helper(cost, i+2, dp))
            return temp
    
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost = [0] + cost
        return self.helper(cost,0,{})
        
        
        
