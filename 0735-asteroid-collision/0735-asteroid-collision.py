class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack=[]
        
        for c in asteroids:
            while stack and stack[-1] > 0 and c < 0:
                diff=c+stack[-1]
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    c=0
                else:
                    c=0
                    stack.pop()
            
            if c:
                stack.append(c)
        
        return stack



                


