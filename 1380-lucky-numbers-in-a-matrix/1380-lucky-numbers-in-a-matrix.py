class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        
        res = []
        hashmap = {}
        
        for r in range(len(matrix)):
            row_min = min(matrix[r])
            i = matrix[r].index(row_min)
            col = []
            for c in range(len(matrix)):
                col.append(matrix[c][i])
            hashmap[row_min] = col
        
        for key, val in hashmap.items():
            if max(val) == key:
                res.append(key)
                
                
        return res
            
                
        