class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        
        hashmap = {}
        res = float("inf")
        
        for i,n in enumerate(nums):
            if n in hashmap:
                hashmap[n].append(i)
            else:
                hashmap[n] = [i]
        
        degree = max(len(val) for val in hashmap.values())
        for ind in hashmap.values():
            if len(ind) == degree:
                res = min(res, (ind[-1] - ind[0])+1)
        return res
        
        
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         hashmap = {}
        
#         for i,n in enumerate(nums):
#             if n in hashmap:
#                 hashmap[n].append(i)
#             else:
#                 hashmap[n] = [i]
        
#         degree = max(len(val) for val in hashmap.values())
        
#         res = len(nums)
        
#         for indices in hashmap.values():
#             if len(indices) == degree:
#                 res = min(res, indices[-1]-indices[0])
        
#         return res+1
        
        
        
        
        
        
        
        
#         if len(nums) == 1:
#             return 1
#         degree_nums = self.degree(nums)
#         print(degree_nums)
#         res = float("inf")
        
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if self.degree(nums[i:j+1]) == degree_nums:
#                     res = min(res, len(nums[i:j+1]))
#         return res
                    
        
        
#     def degree(self, ls):
#         hashmap = {}
#         for num in set(ls):
#             hashmap[num] = ls.count(num)

#         return max(hashmap.values())
        
            
        
        
            
        