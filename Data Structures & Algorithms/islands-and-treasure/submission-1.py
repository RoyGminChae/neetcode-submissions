# reverse graph logic
# dist(a, b) == dist(b, a)

from collections import deque
class Solution:
    
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def bfs(row, col):
            queue = deque()
            queue.append((row, col, 0)) # row, col, level
            while queue:
                row, col, level = queue.popleft()

                if not (0 <= row < ROWS and 0 <= col < COLS):
                    continue

                if grid[row][col] == -1:
                    continue

                if level > grid[row][col]:
                    continue

                grid[row][col] = level
                for a, b in dirs:
                    queue.append((row + a, col + b, level + 1))

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    bfs(row, col)

