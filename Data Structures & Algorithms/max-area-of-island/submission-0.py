class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(row, col):
            if row < 0 or row >= ROWS or col < 0 or col >= COLS:
                return 0
            
            if grid[row][col] == 0:
                return 0
            
            area = 1
            grid[row][col] = 0
            for a, b in directions:
                area += dfs(row + a, col + b)
            
            return area

        area = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    continue
                
                area = max(area, dfs(row, col))

        return area


