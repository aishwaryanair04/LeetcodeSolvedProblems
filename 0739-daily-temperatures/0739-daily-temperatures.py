class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        answer = [0]*len(temperatures)
        
        if len(temperatures) == 1:
            return answer
        
        else:
            stack = []
            for i,t in enumerate(temperatures):
                while stack and t > stack[-1][0]:
                    a = stack.pop()
                    answer[a[1]] = i - a[1]
                stack.append([t,i])
            
        return answer
            
                
                
                
            
        
        