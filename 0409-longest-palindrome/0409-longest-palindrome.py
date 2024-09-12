class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        res = 0
        hashmap = {}
        
        for char in set(s):
            hashmap[char] = s.count(char)
        
        odd = 0
        
        for val in hashmap.values():
            if val % 2 == 0:
                res += val
            else:
                res += (val-1)
                odd += 1
        
        if odd > 0:
            return res + 1
        else:
            return res
            
        
    
                
                
        
        
            
        
        