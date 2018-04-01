class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        i = 0
        while i< len(asteroids):
            asteroid = asteroids[i]
            i += 1
            if stack and stack[-1] > 0 and asteroid < 0: #collision
                if abs(asteroid) > stack[-1]: #bigger asteroid
                    stack.pop()
                    i -= 1
                elif abs(asteroid) == stack[-1]: #equal opposite asteroid
                    stack.pop()
            else: #no collision
                stack.append(asteroid)
                        
        return stack
