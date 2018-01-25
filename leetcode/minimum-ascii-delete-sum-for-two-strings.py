class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        m = len(s1) + 1
        n = len(s2) + 1
        result = [[0]*n for i in range(m)]
        
        for i in range(1, m): result[i][0] += result[i-1][0] + ord(s1[i-1])
        for j in range(1, n): result[0][j] += result[0][j-1] + ord(s2[j-1])
        
        for i in range(1, m):
            for j in range(1, n):
                if s1[i-1] == s2[j-1]:
                    result[i][j] = result[i-1][j-1]
                else:
                    result[i][j] = min(ord(s1[i-1])+result[i-1][j], ord(s2[j-1])+result[i][j-1])
        return result[m-1][n-1]
                
