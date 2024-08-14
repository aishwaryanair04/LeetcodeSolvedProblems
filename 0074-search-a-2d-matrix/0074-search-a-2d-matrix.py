class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        top = 0
        bot = rows-1
        
        while top <= bot:
            row = (top + bot)//2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        
        if top > bot:
            return False
        
        l, r = 0, cols - 1
        
        while l <= r:
            mid = (l + r)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False
                
        
        
        
        
        
        
        
        
        
        
        
        
#         row = 0

#         while row < len(matrix):
#             if matrix[row][0] == target or matrix[row][-1] == target:
#                 return True
#             elif matrix[row][0] < target and matrix[row][-1] > target:
#                 return self.binarySearch(matrix[row], target)
            
#             row += 1
#         return False

        
#     def binarySearch(self, nums, target):
#         low = 0
#         high = len(nums)-1

#         while low <= high:
#             mid = (low+high)//2
#             if nums[mid] == target:
#                 return True
#             elif nums[mid] < target:
#                 low += 1
#             else:
#                 high -= 1
            
#         return False
        
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
        
        
                
        