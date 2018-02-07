class Solution(object):
    def helper(self, n, map):
        if map.has_key(n):
            return map[n]

        result = 1
        if n%2 == 0:
            result += self.helper(n/2, map)
        else:
            result += min(self.helper(n-1, map), self.helper(n+1, map))
        map[n] = result
        return result
    
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        map = {}
        map[0] = 0
        map[1] = 0
        return self.helper(n, map)
        
    
        
