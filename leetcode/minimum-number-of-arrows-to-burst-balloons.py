class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not len(points):
            return 0
        
        def overlap(i1, i2):
            return ((i2[0] <= i1[0] <= i2[1]) or (i1[0] <= i2[0] <= i1[1]))
        
        intervals =  sorted(points, key=lambda x: x[0])
        results = []
        merge = intervals[0]
        for temp in intervals[1:]:
            if overlap(temp, merge):
                merge[1] = min(merge[1], temp[1])
                merge[0] = max(merge[0], temp[0])
            else:
                results.append(merge)
                merge = temp
        results.append(merge)
        return len(results)
