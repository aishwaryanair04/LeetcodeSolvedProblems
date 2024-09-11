class Solution:
    def climbStairs(self, n: int) -> int:
        
        def dp(n, arr):
            if n <= 1:
                return 1
            
            if arr[n] != -1:
                return arr[n]
            arr[n] = dp(n-1, arr) + dp(n-2, arr)
            return arr[n]
        
        arr = [-1] * (n+1)
        return dp(n, arr)
        
        
            
            
            
            
    
        
#         one, two = 1, 1
        
#         for i in range(n - 1):
#             temp = one
#             one = one + two
#             two = temp
        
#         return one
        

        