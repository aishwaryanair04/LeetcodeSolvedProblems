class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        setNums = set(nums)
        
        for num in setNums:
            if nums.count(num) != 2:
                return num
        