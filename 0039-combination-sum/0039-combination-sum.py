class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        
        def dfs(i, subset, currSum):
#             base case1:
            if currSum == target:
                res.append(subset.copy())
                return
#             base case2:
            if i >= len(candidates) or currSum > target:
                return
            
            #Decision to add candidates[i]:
            subset.append(candidates[i])
            dfs(i, subset, currSum + candidates[i])
            
            
            #Decision to not add candidates[i]:
            subset.pop()
            dfs(i+1, subset, currSum)
        
        dfs(0, [], 0)
        return res
            
            
            
            
            
        