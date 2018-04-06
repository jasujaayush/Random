class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rows = len(matrix)
        if not rows:
            return []
        cols = len(matrix[0])
        
        diags = [[] for _ in range(rows+cols-1)]
        for r in range(rows):
            for c in range(cols):
                diags[r+c].append(matrix[r][c])
                
        nums = []
        for i, diag in enumerate(diags):
            nums += diag if i%2 == 1 else diag[::-1]
        return nums
