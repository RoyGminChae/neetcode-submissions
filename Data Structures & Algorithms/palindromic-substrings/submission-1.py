# dp version
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        
        # dp[i][j] = True if dp[i + 1][j - 1] and s[i] == s[j]

        # x s s
        #   x s
        #     x

        res = 0
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 1 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    res += 1
        
        return res