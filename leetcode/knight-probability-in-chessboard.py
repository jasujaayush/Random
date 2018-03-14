class Solution(object):
    def knightProbability(self, Dim, N, i, j):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        m = n = Dim
        mem = [[0 for _ in range(n)] for _ in range(m)]
        mem[i][j] = 1.0
        
        for _ in range(N):
            cur = mem
            mem = [[0 for _ in range(n)] for _ in range(m)]
            for r, row in enumerate(cur):
                for c, val in enumerate(row):
                    for nr, nc in ((r+2, c-1),(r+2, c+1), (r-2, c-1),(r-2, c+1),(r+1, c-2),(r-1, c-2), (r-1, c+2),(r+1, c+2)):
                        if 0<=nr<m and 0<=nc<n:
                            mem[nr][nc] += val/8.0
        
        prob = 0
        for r,row in enumerate(mem):
            prob += sum(row)
        return prob
