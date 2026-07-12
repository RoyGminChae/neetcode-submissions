class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        blocks = [[set() for _ in range(3)] for _ in range(3)]

        for r in range(9):
            for c in range(9):
                br = r // 3
                bc = c // 3

                num = str(board[r][c])
                if num == ".":
                    continue
                    
                if num in rows[r] or num in cols[c] or num in blocks[br][bc]:
                    return False

                rows[r].add(num)
                cols[c].add(num)
                blocks[br][bc].add(num)
        
        return True