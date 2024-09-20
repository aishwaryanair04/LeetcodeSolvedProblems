class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        def dfs(i, word):
            if i >= len(arr):
                return len(word)
            
            if len(word+arr[i]) == len(set(word+arr[i])):
                return max(dfs(i+1, word+arr[i]), dfs(i+1, word))
            
            else:
                return dfs(i+1, word)
        
        return dfs(0, "")
            
            
                    
                
        
        
                
        