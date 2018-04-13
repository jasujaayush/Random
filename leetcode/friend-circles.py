
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        visited = [False for _ in range(len(M))]
        def dfs(i):
            if visited[i]:
                return 0
            
            visited[i] = True
            for j,nbr in enumerate(M[i]):
                if nbr==1:
                    dfs(j)
            return 1
        
        count = 0
        for i in range(len(M)):
            count += dfs(i)
        return count
            
            
        
