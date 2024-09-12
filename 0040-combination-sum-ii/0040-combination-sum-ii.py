class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()  # Sort the candidates to handle duplicates easily
        
        def dfs(i, arr, total):
            if total == target:
                res.append(arr.copy())
                return
            
            if total > target:
                return
            
            for j in range(i, len(candidates)):
                # Skip duplicates
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                
                # Add the current candidate and explore further
                dfs(j + 1, arr + [candidates[j]], total + candidates[j])
        
        dfs(0, [], 0)
        return res
                
        