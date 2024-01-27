class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        stackS, stackT = [], []
        
        for letter in s:
            if letter == "#":
                if stackS != []:
                    stackS.pop()
            if letter != "#":
                stackS.append(letter)
        
        s = ''.join(stackS)
        
        for letter in t:
            if letter == "#":
                if stackT != []:
                    stackT.pop()
            if letter != "#":
                stackT.append(letter)
        
        t = ''.join(stackT)
        
        return s == t
        
        