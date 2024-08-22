class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        if len(nums) < k:
            return []
        
        q = collections.deque()
        res = []
        
        l = 0
        
        for r in range(len(nums)):
            while q and nums[r] > q[-1]:
                q.pop()
            q.append(nums[r])
            
            if (r - l + 1) == k:
                res.append(q[0])
                if nums[l] == q[0]:
                    q.popleft()
                l += 1
                    
        return res
        
            
            