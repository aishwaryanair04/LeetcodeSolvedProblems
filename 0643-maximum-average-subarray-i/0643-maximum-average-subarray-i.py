class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        l = 0
        maxAvg = float("-inf")
        window = []
        currSum = 0
        
        for r in range(len(nums)):
            window.append(nums[r])
            currSum += nums[r]
            if len(window) == k:
                maxAvg = max(maxAvg, (currSum/k))
                print(maxAvg)
                window.remove(nums[l])
                currSum -= nums[l]
                print(currSum)
                l += 1
        
        return maxAvg
                
            
            
            
        
        
        