class Solution(object):
    def neighbors(self, board, i, j):
        liveneighbors = 0
        for x in range(-1, 2):
            for y in range(-1, 2):
                if x==0 and y==0:
                    continue
                r = i + x
                c = j + y
                if r>=0 and r<len(board) and c>=0 and c<len(board[0]) and board[r][c]&1:
                    liveneighbors += 1
        return liveneighbors
    
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        if not rows:
            return
        cols = len(board[0])
        
        for i in range(rows):
            for j in range(cols):
                padosi = self.neighbors(board, i, j)
                if board[i][j] == 1 and (padosi == 3 or padosi == 2):
                    board[i][j] = 3
                elif board[i][j] == 0 and padosi == 3:
                    board[i][j] = 2
                    
        for i in range(rows):
            for j in range(cols):          
                board[i][j] = board[i][j] >> 1
                
