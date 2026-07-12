class Solution:
    def climbStairs(self, n: int) -> int:
        dp = dict()

        def opt(n):
            if n <= 0:
                return 0

            if n == 1:
                return 1

            if n == 2:
                return 2

            if n in dp:
                return dp[n]

            dp[n] = opt(n-1) + opt(n-2)
            return dp[n]
        
        return opt(n)