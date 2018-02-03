class Solution(object):
    def dfs(self, board, row, col):
        queue = [(row, col)]
        while len(queue) > 0:
            row, col = queue.pop()
            board[row][col] = "0"
            neighbors = self.neighbors(board, row, col)
            for (r,c) in neighbors:
                if board[r][c] == "1":
                    queue.append((r,c))
            #print row, col, component, queue
                
    
    def neighbors(self, board, row, col):
        return [(r, c) for (r, c) in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)] if -1 < r < len(board) and -1<c < len(board[0])]
    
    def numIslands(self, board):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(board) == 0:
            return 0
        
        connectedComponents = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "1":
                    self.dfs(board,i,j)
                    connectedComponents += 1
        return connectedComponents
        
        
