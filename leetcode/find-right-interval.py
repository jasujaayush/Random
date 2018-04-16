# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        results = [-1 for _ in range(len(intervals))]
        sorted_intervals = [(x.start, i) for i, x in enumerate(intervals)]
        sorted_intervals.sort()
        
        for i,x in enumerate(intervals):
            r = bisect.bisect_left(sorted_intervals,(x.end,))
            if r<len(intervals):
                results[i] = sorted_intervals[r][1]
        return results
        
