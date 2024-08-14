class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        
        row = 0

        while row < len(matrix):
            if matrix[row][0] == target or matrix[row][-1] == target:
                return True
            elif matrix[row][0] < target and matrix[row][-1] > target:
                return self.binarySearch(matrix[row], target)
            
            row += 1
        return False

        
    def binarySearch(self, nums, target):
        low = 0
        high = len(nums)-1

        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                low += 1
            else:
                high -= 1
            
        return False
        
#         for valueSet in matrix:
#             if self.searchRow(valueSet, target):
#                 return True
            
#         return False
        
    
#     def searchRow(self, row, target):
        
#         low = 0
#         high = len(row) - 1
        
#         while low <= high:
#             mid = (low + high)//2
#             print(low,mid,high)
#             if row[mid] == target:
#                 return True
            
#             elif target > row[mid]:
#                 low = low + 1
            
#             else:
#                 high = high - 1
        
        
                
        