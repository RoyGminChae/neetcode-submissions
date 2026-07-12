class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def opt(i, j):
            if i <= 0 or j <= 0:
                return 1

            if (i, j) in memo:
                return memo[(i, j)]

            memo[(i, j)] = opt(i - 1, j) + opt(i, j - 1) 
            return memo[(i, j)]
        
        return opt(m - 1, n - 1)