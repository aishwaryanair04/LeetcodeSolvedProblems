class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        joined = ""
        
        for num in digits:
            joined += str(num)
        
        plusOne = str(int(joined) + 1)
        
        res = []
        
        for char in plusOne:
            res.append(int(char))
        
        return res
            
        
        
        