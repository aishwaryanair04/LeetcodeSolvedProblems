class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) % 2 != 0:
            return False
        
        targetSum = sum(nums) // 2
        
        dp = set()
        dp.add(0)
        
        for i in range(len(nums)):
            nextDP = set()
            for t in dp:
                nextDP.add(t + nums[i])
                nextDP.add(t)
            
            dp = nextDP
        
        return True if targetSum in dp else False
                
            
            
            
        
        
        
        
        