class Solution:
    # run dfs on every "O" on the perimeters
    # return everything else as "X"
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        visited = set()

        def dfs(row, col):
            if not (0 <= row < ROWS and 0 <= col < COLS):
                return

            if board[row][col] == "X":
                return
            
            if (row, col) in visited:
                return

            visited.add((row, col))
            for dr, dc in directions:
                dfs(row + dr, col + dc)
            
        for col in range(COLS):
            dfs(0, col)
            dfs(ROWS - 1, col)

        for row in range(1, ROWS - 1):
            dfs(row, 0)
            dfs(row, COLS - 1)

        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) not in visited:
                    board[row][col] = "X"






