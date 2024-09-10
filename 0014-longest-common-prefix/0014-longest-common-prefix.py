class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        res = ""
        comp = min(strs, key = len)
        
        for i in range(len(comp)):
            for val in strs:
                if val[i] != comp[i]:
                    return res
            res += comp[i]
        return res
                
                    
        
  
            
        