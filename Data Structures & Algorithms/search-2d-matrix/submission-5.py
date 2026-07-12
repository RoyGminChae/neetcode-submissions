class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0]) 

        top = 0
        bottom = m - 1
        foundRow = None
        while top <= bottom:
            row = (top + bottom) // 2
            if matrix[row][0] <= target <= matrix[row][n - 1]:
                foundRow = row
                break
            elif target > matrix[row][n - 1]:
                top = row + 1
            else:
                bottom = row - 1
       
        if foundRow is None:
            return False

        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            if target == matrix[foundRow][mid]:
                return True
            elif target > matrix[foundRow][mid]:
                left = mid + 1
            else:
                right = mid - 1
        
        return False







