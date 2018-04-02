class Solution(object):
    def helper(self, sofar, row):
        if not sofar:
            return row
        
        dp = []
        for i, val in enumerate(row):
            if i==0:
                dp.append(val + sofar[i])
            elif i == len(row)-1:
                dp.append(val + sofar[i-1])
            else:
                dp.append(val + min(sofar[i-1], sofar[i]))
        return dp
            
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        sofar = []
        for row in triangle:
            sofar = self.helper(sofar, row)
        return min(sofar)
