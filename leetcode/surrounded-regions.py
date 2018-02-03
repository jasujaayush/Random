class Solution(object):
    def dfs(self, board, row, col):
        queue = [(row, col)]
        while len(queue) > 0:
            row, col = queue.pop()
            board[row][col] = 'B' #cells connected to boundary element 'O' are marked as 'B'
            neighbors = self.neighbors(board, row, col)
            for (r,c) in neighbors:
                if board[r][c] == 'O':
                    queue.append((r,c))
            #print row, col, component, queue
                
    
    def neighbors(self, board, row, col):
        return [(r, c) for (r, c) in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)] if -1 < r < len(board) and -1<c < len(board[0])]
    
    
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) == 0 or len(board[0]) == 0:
            return
        
        
        for r in range(0,len(board)):
            for c in (0,len(board[0])-1):
                if board[r][c] == 'O':
                    self.dfs(board,r,c)
                    
        for r in (0,len(board)-1):
            for c in range(0,len(board[0])):
                if board[r][c] == 'O':
                    self.dfs(board,r,c)
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'B':
                    board[r][c] = 'O'
        
