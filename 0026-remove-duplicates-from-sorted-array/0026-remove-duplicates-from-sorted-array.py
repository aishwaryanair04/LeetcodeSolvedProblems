class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        l = 0
        while l < len(nums):
            if l > 0 and nums[l] == nums[l-1]:
                nums.remove(nums[l])
            else:
                l += 1
        return len(nums)
        