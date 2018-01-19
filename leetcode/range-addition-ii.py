class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if len(ops) == 0:
            return m*n
        
        rm = min([x for x,y in ops])
        cm = min([y for x,y in ops])
        return rm*cm
