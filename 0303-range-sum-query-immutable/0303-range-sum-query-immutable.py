class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        
        

    def sumRange(self, left: int, right: int) -> int:
        sumVal = 0
        for i in range(left, right+1):
            sumVal += self.nums[i] 
        return sumVal
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)