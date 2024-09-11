class Solution:
    def fib(self, n: int) -> int:
        
#         def dp(n, arr):
#             if n <= 1:
#                 return n
#             if arr[n] != -1:
#                 return arr[n]
#             arr[n] = dp(n-1, arr) + dp(n-2, arr)
#             return arr[n]
        
#         arr = [-1] * (n+1)
#         return dp(n, arr)
        
        # BASE CASE
        if n <= 1:
            return n
        
        
        # RECURSIVE CASE
        return self.fib(n-1) + self.fib(n-2)
        