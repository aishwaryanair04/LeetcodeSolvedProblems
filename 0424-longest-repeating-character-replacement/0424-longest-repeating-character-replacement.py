class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        hashmap = {}
        l = 0
        maxf = 0
        res = 0
        
        for r in range(len(s)):
            if s[r] in hashmap.keys():
                hashmap[s[r]] += 1
            else:
                hashmap[s[r]] = 1
            maxf = max(maxf, hashmap[s[r]])
            
            while (r - l + 1) - maxf > k:
                hashmap[s[l]] -= 1
                l += 1
                
            res = max(res, (r - l + 1))
        
        return res
                
            
            
            
        