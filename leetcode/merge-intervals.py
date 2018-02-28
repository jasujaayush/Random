# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not len(intervals):
            return []
        
        intervals =  sorted(intervals, key=lambda x: x.start)
        results = []
        merge = intervals[0]
        for temp in intervals[1:]:
            if temp.start <= merge.end:
                merge.end = max(merge.end, temp.end)
            else:
                results.append(merge)
                merge = temp
        results.append(merge)
        return results
            
            
