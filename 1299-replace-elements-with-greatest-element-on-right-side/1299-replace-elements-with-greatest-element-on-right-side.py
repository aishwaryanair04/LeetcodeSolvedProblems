class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        rightMax = -1
        
        for i in range(len(arr)-1, -1, -1):
            
            if i == len(arr)-1:
                print(arr)
                rightMax = arr[i]
                arr[i] = -1

            else:
                temp = arr[i]
                arr[i] = rightMax
                if temp >= rightMax:
                    rightMax = temp
        return arr
                
                
        
        
#         for i in range(len(arr) - 1):
#             arr[i] = max(arr[i+1:])
        
#         arr[-1] = -1
        
#         return arr
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            



        
            
                    
        