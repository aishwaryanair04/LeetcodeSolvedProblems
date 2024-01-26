class Solution:
    def countBits(self, n: int) -> List[int]:
        self.n = n
        res = []
        print(self.findBinary(8))
        for i in range(n+1):
            count = self.findBinary(i).count(1)
            res.append(count)
        return res
            
    
    def findBinary(self, num):
        self.num = num
        self.binary = []
        
        while (num//2) != 0:
            self.binary.append(num % 2)
            num = num//2
        self.binary.append(num%2)
        self.binary.reverse()
        return self.binary
    
        
    
        
        
        
        
        
    
        
        