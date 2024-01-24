class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        listS = s.split(" ")
        temp = []
        print(listS)
        
        for char in listS:
            if char.isalpha():
                temp.append(char)
                
                
        
        return len(temp[-1])
        