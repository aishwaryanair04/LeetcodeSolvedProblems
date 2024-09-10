class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums
        
        l = 0
        r = l+1
        
        while l <= r < len(nums):
            if nums[l] != 0:
                l += 1
  
            if nums[r] != 0 and nums[l] == 0:
                nums[l], nums[r] = nums[r], nums[l]
            
            r += 1
        

                
        