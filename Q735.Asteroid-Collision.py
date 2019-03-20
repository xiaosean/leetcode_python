class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        pos = 0
        n = len(asteroids)
        if n == 0:
            return []
        stack = []

        while pos < n:
            asteroid = asteroids[pos]
            if stack:
                top = stack[-1]
#                 will meet
                if top > 0 and asteroid < 0:
                    if abs(top) < abs(asteroid):
                        stack.pop()
                    elif abs(top) == abs(asteroid):
                        pos += 1 
                        stack.pop()
                    else:
                        pos += 1 
                        
                else:
                    pos += 1 
                    stack += [asteroid]
            else:
                stack += [asteroid]
                pos += 1    
        
        return stack
                    