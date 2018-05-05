class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        dist = [len(S) for _ in range(len(S))]
        for i, c in enumerate(S):
            if c == C:
                for j in range(i+1):
                    dist[j] = min(dist[j], i-j)
        S = S[::-1]
        for i, c in enumerate(S):
            if c == C:
                for j in range(i+1):
                    dist[len(S)-j-1] = min(dist[len(S)-j-1], i-j)
        
        return dist
        
