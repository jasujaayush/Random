class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        pq = []
        edges = [[] for _ in range(N+1)]
        
        final = set()
        for time in times:
            edges[time[0]].append((time[1], time[2]))
        
        heapq.heappush(pq, (0,K))
        
        res = 0
        while len(pq) and len(final) != N:
            min_node = heapq.heappop(pq)
            res = min_node[0]
            s = min_node[1]
            final.add(s)
            for t, w in edges[s]:
                if t not in final:
                    heapq.heappush(pq, (res+w,t))
                    
        if len(final) == N:
            return res
        
        return -1
        
        
        
        
        
