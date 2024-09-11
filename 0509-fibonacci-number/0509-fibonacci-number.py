class Solution:
    def fib(self, n: int) -> int:
        
        if n <= 1:
            return n
        
        prev2 = 0
        prev = 1
        
        for i in range(2, n+1):

            curr = prev2 + prev
            prev2 = prev
            prev = curr
        
        return prev
            
        
#         def dp(n, arr):
#             if n <= 1:
#                 return n
#             if arr[n] != -1:
#                 return arr[n]
#             arr[n] = dp(n-1, arr) + dp(n-2, arr)
#             return arr[n]
        
#         arr = [-1] * (n+1)
#         return dp(n, arr)
        
#         # BASE CASE
#         if n <= 1:
#             return n
        
        
#         # RECURSIVE CASE
#         return self.fib(n-1) + self.fib(n-2)
        