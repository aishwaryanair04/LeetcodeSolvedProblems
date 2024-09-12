class Solution:
    def reverseVowels(self, s: str) -> str:
        
        vowels = ""
        res = ""
        
        for char in s:
            if char in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
                vowels += char
        
        vowels = vowels[::-1]
        j = 0
        
        for char in s:
            if char in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
                res += vowels[j]
                j += 1
            else:
                res += char
        return res
        
        
            
        
        