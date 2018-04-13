class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0
        
        def dfs(r,c):
            if mem[r][c]:
                return mem[r][c]
            
            for i,j in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
                if rows>i>=0 and cols>j>=0 and matrix[i][j] > matrix[r][c]:
                    mem[r][c] = max(mem[r][c], dfs(i,j)+1)
            
            return mem[r][c]
            
        
        rows, cols = len(matrix), len(matrix[0])
        mem = [[0 for _ in range(cols)] for _ in range(rows)]
        maxima = 0
        for r in range(rows):
            for c in range(cols):
                maxima = max(maxima, dfs(r,c))
        
        return maxima+1
