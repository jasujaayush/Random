class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        cycles = N/2
        for i in range(cycles):
            for j in range(i,N-i-1):
                matrix[i][j], matrix[j][N-i-1], matrix[N-i-1][N-j-1], matrix[N-j-1][i] = matrix[N-j-1][i],  matrix[i][j], matrix[j][N-i-1], matrix[N-i-1][N-j-1]
