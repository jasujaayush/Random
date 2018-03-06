class Solution(object):
    def combinationSum(self, nums, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        dp = collections.defaultdict(list)
        dp[0] = []
        
        for n in nums:
            for x in range(target+1):
                    if x-n == 0:
                        dp[x].append([n])
                    elif x-n>=0:
                        for l in dp[x-n]:
                            dp[x].append(l + [n])

