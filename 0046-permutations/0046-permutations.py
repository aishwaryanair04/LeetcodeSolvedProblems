class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        
        #base case:
        if len(nums) == 1:
            return [nums.copy()]
        
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            
            print("perms",perms)
            for perm in perms:
                print("perm",perm)
                perm.append(n)
                res.append(perm)
            
            nums.append(n)
        
        return res
        
        
            
            
            
            
            
        