class Solution:
    # 1D top-down
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = dict()        

        def opt(amount):
            if amount < 0:
                return float("inf")

            if amount == 0:
                return 0
            
            if amount in dp:
                return dp[amount]
            
            res = float("inf")
            for coin in coins:
                res = min(res, opt(amount - coin) + 1)

            dp[amount] = res
            return dp[amount]

        return opt(amount) if opt(amount) != float("inf") else -1