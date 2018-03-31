class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        ad = collections.defaultdict(list)
        for dep in prerequisites:
            ad[dep[0]].append(dep[1])
        
        def dfs(course):
            if visited[course]:
                return False
            if done[course]: 
                return True
            
            visited[course] = True
            for dep in ad[course]:
                if not dfs(dep): return False
            visited[course] = False
            done[course] = True
            return True
        
        visited = [False for _ in range(numCourses)]
        done = [False for _ in range(numCourses)]
        for course in range(numCourses):
            if not dfs(course): return False
        
        return True
                
