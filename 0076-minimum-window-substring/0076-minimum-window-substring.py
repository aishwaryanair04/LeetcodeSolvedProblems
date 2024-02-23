class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if t == "":
            return ""
        
        hashmapT = {}
        for char in set(t):
            hashmapT[char] = t.count(char)
        
        hashmapW = {}
        have = 0
        need = len(hashmapT)
        res, resLen = [-1,-1], float('inf')
        l = 0
        for r in range(len(s)):
            hashmapW[s[r]] = 1 + hashmapW.get(s[r],0)
            if s[r] in hashmapT and hashmapW[s[r]] == hashmapT[s[r]]:
                have += 1
            
            while have == need:
                if (r-l+1) < resLen:
                    res = [l,r]
                    resLen = r-l+1
                
                hashmapW[s[l]] -= 1
                if s[l] in hashmapT and hashmapW[s[l]] < hashmapT[s[l]]:
                    have -= 1
                l += 1
        
        l,r = res
        return s[l:r+1] if resLen != float('inf') else  ""
                    
                
                
                
                
                
           
        
        
        
        
        
        
        
        
        
        
#         hashmapT = {}
#         for char in set(t):
#             hashmapT[char] = t.count(char)
        
#         hashmapW = {}
#         need = len(hashmapT)
#         res = []
#         l = 0
#         window = []
#         for r in range(len(s)):
#             window.append(s[r])
#             if s[r] in t:
#                 if s[r] not in hashmapW:
#                     hashmapW[s[r]] = 1
#                 else:
#                     hashmapW[s[r]] += 1
            
#             if len(hashmapW) == need:
#                 print(window)
#                 res.append(''.join(window.copy()))
#                 window.remove(s[l])
#                 if s[l] in hashmapW:
#                     if hashmapW[s[l]] == 1:
#                         hashmapW.pop(s[l])
#                     else:
#                         hashmapW[s[l]] -= 1
#                 l += 1
#         print(res)
#         while l < r:
#             if len(hashmapW) == need:
#                 res.append(''.join(window.copy()))
#                 window.remove(s[l])
#                 if s[l] in hashmapW:
#                     if hashmapW[s[l]] == 1:
#                         hashmapW.pop(s[l])
#                     else:
#                         hashmapW[s[l]] -= 1
#             l += 1
            
#         if res == []:
#             return ""
        
#         length,word = 0,""
#         for value in res:
#             if length == 0:
#                 length = len(value)
#                 word = value
#             else:
#                 if len(value) < length:
#                     length = len(value)
#                     word = value
#         return word
            
            
                
                    
            
            
                
        
        
            
            
                    
                    
        
        