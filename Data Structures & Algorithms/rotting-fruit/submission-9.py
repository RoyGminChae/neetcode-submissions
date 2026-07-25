from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        queue = deque()
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    queue.append((row, col))
        
        time = 0
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()

                for dr, dc in directions:
                    nextRow = row + dr 
                    nextCol = col + dc

                    if not (0 <= nextRow < ROWS and 0 <= nextCol < COLS):
                        continue

                    if grid[nextRow][nextCol] != 1:
                        continue

                    grid[nextRow][nextCol] = 2
                    queue.append((nextRow, nextCol))

            time += 1

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    return -1
        
        return max(0, time - 1)
        