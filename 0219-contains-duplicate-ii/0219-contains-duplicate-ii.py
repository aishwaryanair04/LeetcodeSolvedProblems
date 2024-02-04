class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        window = set()
        L = 0
        
        for R in range(len(nums)):
            if abs(R-L) > k:
                window.remove(nums[L])
                L += 1
            if nums[R] in window:
                return True
            window.add(nums[R])
        return False

        
        
#         time limit exceeds in below:
        
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j] and abs(i - j) <=k:
        #             return True
        # return False
        