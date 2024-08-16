class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        stack = []
        
        for letter in s:
            if stack:
                if stack[-1] == letter:
                    stack.pop()
                else:
                    stack.append(letter)
            else:
                stack.append(letter)
        
        return "".join(stack)
        