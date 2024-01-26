class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixArray = []
        curr = 0
        for val in nums:
            curr += val
            self.prefixArray.append(curr)
            
    def sumRange(self, left: int, right: int) -> int:
        if left > 0:
            val = self.prefixArray[right] - self.prefixArray[left-1]
            return val
        else:
            return self.prefixArray[right]
            
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)