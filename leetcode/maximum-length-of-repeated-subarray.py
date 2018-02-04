class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        lena = len(A)
        lenb = len(B)
        results = [[0 for x in range(lenb+1)] for x in range(lena+1)]
        best = 0
        for i in range(lena-1, -1, -1):
            for j in range(lenb-1, -1, -1):
                if A[i] == B[j]:
                    results[i][j] = (1 + results[i+1][j+1])
                    best = max(best, results[i][j])
        return best
            
        
