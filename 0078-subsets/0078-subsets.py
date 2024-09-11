class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        
        def subs(i, arr):
            if i >= len(nums):
                res.append(arr.copy())
                return
            
            arr.append(nums[i])
            subs(i+1, arr)
            arr.remove(nums[i])
            subs(i+1, arr)
        
        subs(0, [])
        return res
        
        
#         res = []
        
#         subset = []
        
#         def dfs(i):
#             if i >= len(nums):
#                 res.append(subset.copy())
#                 return
            
#             #Decision to include nums[i]:
#             subset.append(nums[i])
#             dfs(i + 1)
            
            
#             #Decision to not include nums[i]:
#             subset.pop()
#             dfs(i + 1)
        
#         dfs(0)
#         return res
            
            
        