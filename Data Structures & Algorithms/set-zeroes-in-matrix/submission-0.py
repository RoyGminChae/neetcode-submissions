class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row0 = 1
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] != 0:
                    continue

                matrix[0][col] = 0
                if row == 0:
                    row0 = 0
                else:
                    matrix[row][0] = 0

        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0

        if matrix[0][0] == 0:
            for row in range(len(matrix)):
                matrix[row][0] = 0

        if row0 == 0:
            for col in range(len(matrix[0])):
                matrix[0][col] = 0




        
        # [[1,0,3],[4,0,5],[6,7,8]]