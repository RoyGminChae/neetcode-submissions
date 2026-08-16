# case 1: exclude last house
# case 2: exclude first house
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def robLinear(arr):
            n = len(arr)
            dp = [0] * n

            dp[0] = arr[0]

            if n == 1:
                return dp[0]

            dp[1] = max(arr[0], arr[1])

            for i in range(2, n):
                dp[i] = max(
                    dp[i - 1],
                    arr[i] + dp[i - 2]
                )

            return dp[-1]

        return max(
            robLinear(nums[:-1]),  # exclude last house
            robLinear(nums[1:])    # exclude first house
        )