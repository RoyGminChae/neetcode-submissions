class Solution:
    # cw 90 degrees = reverse matrix vertically + tranpose
    # ccw 90 degrees = reverse matrix horizontally + tranpose
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix.reverse()
        
        # tranpose
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        

