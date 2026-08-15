class Solution:
    # more similar to dp from CS330
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = dict()

        def opt(i):
            if i == 0:
                return cost[i]

            if i == 1:
                return cost[i]
            
            if i in dp:
                return dp[i]

            dp[i] = cost[i] + min(opt(i - 1), opt(i - 2))
            return dp[i]

        
        return min(opt(len(cost) - 1), opt(len(cost) - 2)) # top is reachable from either of those steps