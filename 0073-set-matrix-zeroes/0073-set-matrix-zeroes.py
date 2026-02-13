class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_row = False
        zero_col = False
        rows, cols = len(matrix), len(matrix[0])

        for x in range(rows):
            if matrix[x][0] == 0:
                zero_col = True
        for y in range(cols):
            if matrix[0][y] == 0:
                zero_row = True

        
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if zero_row:
            for row in range(cols):
                matrix[0][row] = 0
        if zero_col:
            for column in range(rows):
                matrix[column][0] = 0
        


                    
        