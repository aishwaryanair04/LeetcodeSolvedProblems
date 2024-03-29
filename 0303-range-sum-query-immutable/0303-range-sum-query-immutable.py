class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix = []
        for i in range(len(self.nums)):
            if self.prefix != []:
                self.prefix.append(self.nums[i] + self.prefix[-1])
            else:
                self.prefix.append(self.nums[i])
        print(self.prefix)
        
        

    def sumRange(self, left: int, right: int) -> int:
        if left != 0:
            return self.prefix[right] - self.prefix[left-1]
        else:
            return self.prefix[right]
        
        
        # My Solution
        
#         def __init__(self, nums: List[int]):
#         self.prefixArray = []
#         curr = 0
#         for val in nums:
#             curr += val
#             self.prefixArray.append(curr)
            
#         def sumRange(self, left: int, right: int) -> int:
#         if left > 0:
#             val = self.prefixArray[right] - self.prefixArray[left-1]
#             return val
#         else:
#             return self.prefixArray[right]
            
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)