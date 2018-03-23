class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        d = {}
        total_width = 0
        for row in wall:
            s = 0
            for num in row:
                s += num
                d[s] = d.get(s,0) + 1
            total_width = s
        #print d
        
        max_count = 0
        for k in d:
            if k!=total_width and d[k] > max_count:
                max_count = d[k]
        
        return len(wall) - max_count
