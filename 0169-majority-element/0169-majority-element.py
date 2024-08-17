class Solution:
    def majorityElement(self, nums: List[int]) -> int:
    
            
            
        
#         0(1) space, ideal solution:
        
        count, res = 0,0
        
        for n in nums:
            if count == 0:
                res = n
            if res == n:
                count += 1
            else:
                count -= 1
        
        return res
            
            
#         hashmap but 0(n):

#         count = {}
#         res, maxCount = 0,0
        
#         for n in nums:
#             count[n] = 1 + count.get(n, 0)
#             res = n if count[n] > maxCount else res
#             maxCount = max(maxCount, count[n])
        
#         return res
        
#     hashmap but set too:
#         setNums = set(nums)
#         hashmap = {}
        
#         for num in setNums:
#             hashmap[num] = nums.count(num)
        
#         return  max(hashmap, key=lambda k: hashmap[k])
            
        