class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s3) !=  len(s1)+len(s2):
            return False
        
        
        possible = [[False]*(len(s2)+1)]*(len(s1)+1)
        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                if i==0 and j==0:
                    possible[i][j] = True
                elif i==0:
                    possible[i][j] = (possible[i][j-1] and s3[j-1] == s2[j-1])
                elif j==0:
                    possible[i][j] = (possible[i-1][j] and s3[i-1] == s1[i-1])
                else:
                    possible[i][j] = ((possible[i][j-1] and (s3[i+j-1] == s2[j-1])) or (possible[i-i][j] and s3[i+j-1] == s1[i-1]) )
        return possible[len(s1)][len(s2)]
