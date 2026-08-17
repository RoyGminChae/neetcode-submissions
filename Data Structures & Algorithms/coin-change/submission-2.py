class Solution:
    # 2D, bottom up
    # dp[i][amount] = min # of coins to reach amount from index 0 to i
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        INF = float("inf")

        # row: index 0 to index n - 1
        # col: 0, 1, ... , amount
        dp = [[INF] * (amount + 1) for _ in range(n)]

        # amount == 0 requires 0 coins
        for i in range(n):
            dp[i][0] = 0

        # only coins[0]. Only 1 coin
        for val in range(amount + 1):
            if val - coins[0] >= 0:
                dp[0][val] = 1 + dp[0][val - coins[0]]

        for i in range(n):
            for val in range(amount + 1):
                dp[i][val] = dp[i - 1][val] # don't use this coin
                
                # use this coin
                if val - coins[i] >= 0:
                    dp[i][val] = min(dp[i][val], 1 + dp[i][val - coins[i]])

        return dp[n - 1][amount] if dp[n - 1][amount] != INF else -1
                    

        