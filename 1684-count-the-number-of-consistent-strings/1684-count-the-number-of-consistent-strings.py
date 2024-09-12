class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:

        res = 0
        flag = True
        
        for word in words:
            for letter in set(word):
                if letter not in allowed:
                    flag = False
                    break
            
            if flag == True:
                res += 1
            flag = True
        return res
                    
        