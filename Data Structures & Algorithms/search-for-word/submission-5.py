class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visiting = set()
        path = []

        # path = list of char
        # visited = set() of (row, col)
        def dfs(row, col):
            if len(path) == len(word):
                return "".join(path) == word
            
            if not (0 <= row < len(board) and 0 <= col < len(board[0])):
                return False

            if (row, col) in visiting:
                return False

            path.append(board[row][col])
            visiting.add((row, col))
            for dr, dc in dirs:
                if dfs(row + dr, col + dc):
                    return True
            
            path.pop()
            visiting.remove((row, col))

            return False

        for row in range(len(board)):
            for col in range(len(board[0])):
                if dfs(row, col):
                    return True

        return False


        


