class Solution:
    # backtracking + memoization logic
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = dict()

        def opt(i, val):
            if i < 0:
                if val == target:
                    return 1
                else:
                    return 0
            
            if (i, val) in dp:
                return dp[(i, val)]

            dp[(i, val)] = opt(i - 1, val - nums[i]) + opt(i - 1, val + nums[i])
            return dp[(i, val)]

        return opt(len(nums) - 1, 0)