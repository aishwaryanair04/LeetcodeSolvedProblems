class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        if n == 1:
            return True
        if n == 0:
            return False
        
        while n > 1:
            n = n/4
        
        return True if n ==1 else 0
        