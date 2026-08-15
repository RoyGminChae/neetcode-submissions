class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        dp = dict()

        def opt(i):
            if i >= len(cost):
                return 0
            
            if i in dp:
                return dp[i]

            dp[i] = cost[i] + min(opt(i + 1), opt(i + 2))
            return dp[i]

        
        return min(opt(0), opt(1))