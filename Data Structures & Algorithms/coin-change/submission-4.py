class Solution:
    # 2D, top-down
    # dp[i][amount] = min # of coins to reach amount from index 0 to i
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = dict()

        def opt(i, amount):
            if amount == 0:
                return 0

            if amount < 0 or i < 0:
                return float("inf")

            if (i, amount) in dp:
                return dp[(i, amount)]

            skip = opt(i - 1, amount)
            keep = 1 + opt(i, amount - coins[i])

            dp[(i, amount)] = min(skip, keep)

            return dp[(i, amount)]

        res = opt(n - 1, amount)
        return res if res != float("inf") else -1

                    

        