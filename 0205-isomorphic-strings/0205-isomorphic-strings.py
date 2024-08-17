class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if s == t:
            return True
        
        hashmap = {}
        
        for i in range(len(s)):
            if s[i] not in hashmap:
                if t[i] in hashmap.values():
                    return False
                hashmap[s[i]] = t[i]
            else:
                if hashmap[s[i]] == t[i]:
                    continue
                else:
                    return False
        return True
        
        
        