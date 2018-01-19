class Solution(object):
    def find(self, parent, x):
        while parent[x] != x:
            x = parent[x]
        return x
    
    def findRedundantConnection(self, edges):
        N = len(edges)
        parent = [y for y in range(0,N+1)]
        
        for edge in edges:
            x,y = edge
            if self.find(parent, x) == self.find(parent, y):
                return edge
            parent[self.find(parent, y)] = self.find(parent, x)
            
    
         
