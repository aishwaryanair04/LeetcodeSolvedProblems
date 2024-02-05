class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        l = 0
        minL = float("inf")
        sumSA = 0
        
        for r in range(len(nums)):
            sumSA += nums[r]
            while sumSA >= target:
                minL = min(minL, r+1-l)
                sumSA -= nums[l]
                l += 1
        
        return 0 if minL == float("inf") else minL

        
#         l,r = 0,0
#         minL = 0
        
#         while r < len(nums):
#             subarray = nums[l:r+1]
#             if sum(subarray) < target:
#                 r += 1
#             else:
#                 if minL != 0:
#                     minL = min(minL, len(subarray))
#                 else:
#                     minL = len(subarray)
#                 l += 1
        
#         return minL
            
            
            
                
            
            
            
            
        
                
                
            
            
            
        