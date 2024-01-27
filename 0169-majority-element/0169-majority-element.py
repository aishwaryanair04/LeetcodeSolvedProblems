class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        setNums = set(nums)
        hashmap = {}
        
        for num in setNums:
            hashmap[num] = nums.count(num)
        
        return  max(hashmap, key=lambda k: hashmap[k])
            
        