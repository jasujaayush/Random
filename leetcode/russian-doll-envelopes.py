class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        def comp(x,y):
            return 1 if x[0]>y[0] or (x[0] == y[0] and x[1] < y[1]) else -1
            
        dp = [1]*len(envelopes)
        envelopes.sort(cmp=comp)
        #print envelopes
        h = []
        for i, e in enumerate(envelopes):
            index = bisect.bisect_left(h, e[1])
            if index >= len(h):
                h.append(e[1])
            else:
                h[index] = e[1]
        return len(h)
        
