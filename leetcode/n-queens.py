class Solution(object):
    def __init__(self):
        self.results = []
    
    def helper(self, row, pos, n):
        if len(pos) == n:
            self.results.append(pos[:])
            return
            
        for i in range(n):
            isGood = True
            for low, p in enumerate(pos):
                if p[1] == i or (row - low) == abs(p[1] - i): 
                    isGood = False
                    break
            if isGood:
                pos.append((row, i))
                self.helper(row+1, pos, n)
                pos.pop()
            
            
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.helper(0, [], n) 
        results = []
        for res in self.results:
            x = []
            for row, col in res:
                S = ['.']*n
                S[col] = 'Q'
                S = "".join(S)
                x.append(S)
            results.append(x)
        return results
