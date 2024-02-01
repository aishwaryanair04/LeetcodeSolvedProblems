class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        
        if len(original) != m*n:
            return []
        res = []
        
        i = 0
        while i < len(original):
            row = original[i:i+n]
            res.append(row)
            i = i+n

        return res
            
            
            
            
            
                
                
                
                
                
                
            
                
                
            
        