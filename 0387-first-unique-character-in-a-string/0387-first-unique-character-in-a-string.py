class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        hashmap = {}
        res = float("inf")
        
        for letter in set(s):
            hashmap[letter] = s.count(letter)
        
        for key, val in hashmap.items():
            if val == 1:
                res = min(res, s.index(key))
        
        if res != float("inf"):
            return res
        else:
            return -1
        
        
        
        