class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        from bisect import bisect_left as bl
        heaters.sort()
        maxima = 0
        for house in houses:
            assigned, dist = bl(heaters, house), 0
            if assigned == len(heaters): 
                dist = house - heaters[assigned-1]
            elif assigned == 0:
                dist = heaters[assigned] - house
            else:
                dist = min(house - heaters[assigned-1], heaters[assigned] - house)
            maxima = max(maxima, dist)
        
        return maxima
        
        
            
        
