class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        count = defaultdict(int)
        total = 0
        for i in range(len(points)):
            distanceMap = defaultdict(int)
            p1 = points[i]
            for j in range(len(points)):
                if i!=j:
                    p2 = points[j]
                    distance = (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2
                    distanceMap[distance] += 1 
                    
                    
            for key in distanceMap:
                x = distanceMap[key]
                total += x*(x-1)
            
        return total
        
