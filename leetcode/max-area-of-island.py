class Solution(object):
    def traverse(self, grid, i, j):
        if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j] == -1:
            return 0
        area = 0
        if grid[i][j] == 1:
            grid[i][j] = -1
            area += 1 + self.traverse(grid, i-1, j) + self.traverse(grid, i+1, j) + self.traverse(grid, i, j-1) + self.traverse(grid, i, j+1)
        return area
    
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                area = self.traverse(grid, i, j)
                if area > max_area:
                    max_area = area
                
        return max_area
