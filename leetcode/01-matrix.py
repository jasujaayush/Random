class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(matrix)
        if rows == 0:
            return [[]]
        cols = len(matrix[0])
        
        distance = [[10000000000 for _ in range(cols)] for _ in range(rows)]
                
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    distance[i][j] = 0
                else:
                    if i>0:
                        distance[i][j] = min(distance[i][j], 1+distance[i-1][j])
                    if j>0:
                        distance[i][j] = min(distance[i][j], 1+distance[i][j-1])
                        
        for i in range(rows-1, -1,-1):
            for j in range(cols-1,-1,-1):
                if i<rows-1:
                    distance[i][j] = min(distance[i][j], 1+distance[i+1][j])
                if j<cols-1:
                    distance[i][j] = min(distance[i][j], 1+distance[i][j+1])
                
        return distance
