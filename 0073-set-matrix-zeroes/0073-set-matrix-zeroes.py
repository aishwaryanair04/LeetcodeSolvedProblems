class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        if not matrix:
            return []

        m = len(matrix)
        n = len(matrix[0])

        zeroes_row = [False] * m
        zeroes_col = [False] * n
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    zeroes_row[row] = True
                    zeroes_col[col] = True

        for row in range(m):
            for col in range(n):
                if zeroes_row[row] or zeroes_col[col]:
                    matrix[row][col] = 0
        
#         rows, columns = len(matrix), len(matrix[0])
#         rowZero = False
        
#         for r in range(rows):
#             for c in range(columns):
#                 if matrix[r][c] == 0:
#                     matrix[0][c] = 0
#                     if r > 0:
#                         matrix[r][0] = 0
#                     else:
#                         rowZero = True
        
#         for r in range(1, rows):
#             for c in range(1, columns):
#                 if matrix[0][r] == 0 or matrix[r][0] == 0:
#                     matrix[r][c] = 0
        
#         if matrix[0][0] == 0:
#             for r in range(rows):
#                 matrix[r][0] = 0
        
#         if rowZero:
#             for c in range(columns):
#                 matrix[0][c] = 0
        