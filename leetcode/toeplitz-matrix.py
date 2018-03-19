class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        r = len(matrix)
        if not r:
            return True
        
        c = len(matrix[0])
        for i in range(r):
            for j in range(c):
                if i-1 >= 0 and j-1>=0 and matrix[i][j] != matrix[i-1][j-1]:
                    return False
        
        return True
