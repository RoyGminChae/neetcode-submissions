class Solution:
    # backtracking view
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = dict()

        def opt(i, coin): # 
            if i >= n:
                return 0
            
            if (i, coin) in dp:
                return dp[(i, coin)]

            # skip
            res = opt(i + 1, coin)

            # buy
            if not coin:
                res = max(res, -prices[i] + opt(i + 1, True))

            # sell
            if coin:
                res = max(res, prices[i] + opt(i + 2, False))
            
            dp[(i, coin)] = res
            return res

        return opt(0, False)
