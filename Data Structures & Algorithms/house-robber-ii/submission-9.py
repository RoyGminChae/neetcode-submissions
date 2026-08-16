# bottom-up
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if len(nums) == 0:
            return 0
    
        if len(nums) == 1:
            return nums[0]

        dp = [[0] * n for _ in range(2)]
        
        # first house is not robbed
        dp[False][0] = 0
        dp[False][1] = nums[1]

        # first house is robbed
        dp[True][0] = nums[0]
        dp[True][1] = nums[0]

        for i in range(2, len(nums)):
            dp[False][i] = max(dp[False][i - 1], nums[i] + dp[False][i - 2])
            
            if i == len(nums) - 1:
                dp[True][i] = dp[True][i - 1]
            else:
                dp[True][i] = max(dp[True][i - 1], nums[i] + dp[True][i - 2])
            
        
        return max(dp[True][-1], dp[False][-1])

