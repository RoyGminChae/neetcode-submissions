# Reverse Flow logic


# missing (0, 4), (2, 0)
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        pacific = set()
        atlantic = set()

        def dfs(row, col, prevHeight, visited):
            if not (0 <= row < ROWS and 0 <= col < COLS):
                return
            
            if (row, col) in visited:
                return

            currHeight = heights[row][col]
            if currHeight < prevHeight:
                return

            visited.add((row, col))
            print((row, col), visited)
            for dr, dc in directions:
                dfs(row + dr, col + dc, currHeight, visited)
            
        # account for the two shared corners
        for col in range(COLS):
            dfs(0, col, -1, pacific)
            dfs(ROWS - 1, col, -1, atlantic)

        # account for the two shared corners
        for row in range(ROWS):
            dfs(row, 0, -1, pacific)
            dfs(row, COLS - 1, -1, atlantic)

        res = []
        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) in pacific and (row, col) in atlantic:
                    res.append([row, col])

        return res
            
            