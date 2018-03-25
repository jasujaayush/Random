class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        start = [len(S)]*26
        end = [-1]*26
        
        for i, c in enumerate(S):
            j = ord(c) - ord('a')
            start[j] = min(i, start[j])
            end[j] = i
        
        intervals = zip(start, end)
        intervals.sort()
        
        
        results = []
        merge = list(intervals[0])
        for temp in intervals[1:]:
            if temp[0] <= merge[1]:
                merge[1] = max(merge[1], temp[1])
            else:
                if merge[1] - merge[0] + 1 > 0:
                    results.append(merge[1] - merge[0] + 1)
                merge = list(temp)
                                                 
        if merge[1] - merge[0] + 1 > 0:
                    results.append(merge[1] - merge[0] + 1)
        return results
