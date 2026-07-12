class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = dict()
        
        def opt(amount):       
            if amount == 0:
                return 0
            
            if amount in memo:
                return memo[amount]

            res = float('inf')
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + opt(amount - coin))

            memo[amount] = res
            return res
        
        minCoins = opt(amount)
        return -1 if minCoins == float('inf') else minCoins

