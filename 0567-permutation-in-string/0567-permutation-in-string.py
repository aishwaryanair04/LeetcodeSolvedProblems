class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        
        hash1 = {}
        hash2 = {}

        for char in set(s1):
            hash1[char] = s1.count(char)
        
        l = 0
        
        for r in range(len(s2)):
            if s2[r] in hash2:
                hash2[s2[r]] += 1
            else:
                hash2[s2[r]] = 1
            
           
            if (r - l + 1) > len(s1):
                if hash2[s2[l]] == 1:
                    del hash2[s2[l]]
                else:
                    hash2[s2[l]] -= 1
                l += 1
            
            
            
            if hash2 == hash1:
                return True
        
        return False
                
                
        
        
                
                
                        
                
                
                
        