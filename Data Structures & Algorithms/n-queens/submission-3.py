class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 0:
            return []

        unsafeCols = set()
        unsafePosDiag = set() # //: row + col
        unsafeNegDiag = set() # \\: row - col
        board = [["." for _ in range(n)] for _ in range(n)]

        res = []
        def dfs(row):
            if row >= n:
                validBoard = []
                for r in board:
                    validBoard.append("".join(r))
                res.append(validBoard)
                return 

            for col in range(n):
                if (
                    col in unsafeCols 
                    or row + col in unsafePosDiag
                    or row - col in unsafeNegDiag
                ):
                    continue
                
                unsafeCols.add(col)
                unsafePosDiag.add(row + col)
                unsafeNegDiag.add(row - col)
                board[row][col] = "Q"
                
                dfs(row + 1)

                unsafeCols.remove(col)
                unsafePosDiag.remove(row + col)
                unsafeNegDiag.remove(row - col)
                board[row][col] = "."

        dfs(0)
        return res
            

            
            







