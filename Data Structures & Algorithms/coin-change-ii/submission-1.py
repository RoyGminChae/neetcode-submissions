class Solution:
    # unbounded knapsack from CS330
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        if n == 0:
            return 0
        
        dp = dict()

        def opt(i, amount): # number of ways to get this amount from 0 to i
            if i < 0 or amount < 0:
                return 0

            if amount == 0:
                return 1

            if (i, amount) in dp:
                return dp[(i, amount)]

            skip = opt(i - 1, amount)
            take = opt(i, amount - coins[i])
            
            dp[(i, amount)] = skip + take
            return dp[(i, amount)]

        return opt(n - 1, amount)
            