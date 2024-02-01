class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        for fast in range(len(nums)):
            
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]

            if nums[slow] != 0:
                slow += 1
#         if len(nums) == 1:
#             return nums
        
#         l, r = 0, l+1
        
#         while l <= r < len(nums):
#             if nums[l] != 0:
#                 l += 1
#             if nums[r] == 0:
                
        