class Solution:
    def fib(self, n: int) -> int:
        
        # BASE CASE
        if n <= 1:
            return n
        
        
        # RECURSIVE CASE
        return self.fib(n-1) + self.fib(n-2)
        