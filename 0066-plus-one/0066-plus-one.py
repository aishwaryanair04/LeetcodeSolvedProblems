class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        if len(digits) == 1:
            if digits[0] < 9:
                digits[0] += 1
            else:
                digits = [1,0]
        
        else:
            if digits[-1] < 9:
                digits[-1] += 1
            else:
                for i in range(len(digits)-1, -1, -1):
                    print(i)
                    if digits[i] == 9:
                        if i != 0:
                            digits[i] = 0
                            carry = 1
                        else:
                            digits[i] = 0
                            digits = [1] + digits
                    else:
                        digits[i] += 1
                        break
        
        return digits
                        
                    
        
        
        
        