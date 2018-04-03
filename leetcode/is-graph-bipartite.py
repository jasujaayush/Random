class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """ 
        def dfs(node):
            if visited[node]:
                return True
            
            c = color[node]
            visited[node] = True
            for dst in graph[node]:
                if color[dst] == c:
                    return False
                else:
                    color[dst] = 1 - c
                    if not dfs(dst):
                        return False
                    
            return True
        
        color = [None for _ in range(len(graph))]
        visited = [False for _ in range(len(graph))]
        for node in range(len(graph)):
            if color[node] == None:
                color[node] = 0
            if not dfs(node): return False
        
        return True
