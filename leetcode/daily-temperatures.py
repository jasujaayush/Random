class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        n = len(temperatures)
        results = [0 for _ in range(n)]
        for i in range(n):
            while len(stack) > 0 and temperatures[stack[-1]] < temperatures[i]:
                results[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
                
        return results
                    
