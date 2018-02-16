class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        d = {}
        for i,r in enumerate(list1):
            d[r] = i
            
        minima = 10**9
        res = []
        for i,r in enumerate(list2):
            if d.has_key(r) and d[r]+i<=minima:
                if d[r]+i < minima: res = []
                minima = d[r]+i
                res.append(r)
        return res
