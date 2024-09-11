class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        
        def subs(i, arr):
            if i >= len(nums):
                if sorted(arr) not in res:
                    res.append(sorted(arr))
                return
            
            subs(i+1, arr+[nums[i]])
            subs(i+1, arr)
        
        subs(0, [])
        return res
        

        
        