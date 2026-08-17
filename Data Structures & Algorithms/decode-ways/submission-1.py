class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        # dp(i) number of ways to decode s[:i + 1]
        dp = {-1: 1}
        
        for i in range(n):
            dp[i] = 0   

            # single digit case
            if s[i] != "0":
                dp[i] += dp[i - 1]

            # double digit case
            if i > 0 and 10 <= int(s[i - 1:i + 1]) <= 26:
                dp[i] += dp[i - 2]

        return dp[len(s) - 1]