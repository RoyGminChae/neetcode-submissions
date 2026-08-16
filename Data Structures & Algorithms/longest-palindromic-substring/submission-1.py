# dp method
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        
        # dp[i][j] = True if dp[i + 1][j - 1] and s[i] == s[j]

        # x s s
        #   x s
        #     x

        resIndex = 0
        resLength = 0
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 1 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if j - i + 1 > resLength:
                        resIndex = i
                        resLength = j - i + 1
        
        return s[resIndex: resIndex + resLength]

        

