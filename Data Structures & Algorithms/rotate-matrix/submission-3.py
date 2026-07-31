class Solution:
    # method 1:
    # outer square to inner square
    # 


    # method 2:
    # cw 90 degrees = reverse matrix vertically + tranpose
    # ccw 90 degrees = reverse matrix horizontally + tranpose
    def rotate(self, matrix: List[List[int]]) -> None:
        left, right = 0, len(matrix) - 1
        while left < right:
            top, bottom = left, right
            for i in range(right - left):
                (
                    matrix[top][left + i], 
                    matrix[top + i][right], 
                    matrix[bottom][right - i], 
                    matrix[bottom - i][left]
                ) = (
                    matrix[bottom - i][left],
                    matrix[top][left + i],
                    matrix[top + i][right],
                    matrix[bottom][right - i]
                )
            
            left += 1
            right -= 1
        

            


    # def rotate(self, matrix: List[List[int]]) -> None:
    #     matrix.reverse()
        
    #     # tranpose
    #     for i in range(len(matrix)):
    #         for j in range(i + 1, len(matrix)):
    #             matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        