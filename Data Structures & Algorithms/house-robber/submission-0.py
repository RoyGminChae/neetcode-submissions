class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = dict()
        
        def opt(i):
            if i < 0:
                return 0
    
            if i in dp:
                return dp[i]

            dp[i] = max(opt(i - 1), nums[i] + opt(i - 2))
            return dp[i]
        
        return opt(len(nums) - 1)