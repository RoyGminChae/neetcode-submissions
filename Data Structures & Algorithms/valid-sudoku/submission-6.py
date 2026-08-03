class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowCheck = [set() for _ in range(9)]
        colCheck = [set() for _ in range(9)]
        blockCheck = [[set() for _ in range(3)] for _ in range(3)]

        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val == ".":
                    continue

                if val in rowCheck[row] or val in colCheck[col] or val in blockCheck[row // 3][col // 3]:
                    return False

                rowCheck[row].add(val)
                colCheck[col].add(val)
                blockCheck[row // 3][col // 3].add(val)
        
        return True

