# end in i dp version
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = dict()
        dp[0] = 1
 
        for i in range(len(nums)):
            LIS = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    LIS = max(LIS, 1 + dp[j])
            
            dp[i] = LIS

        return max(dp.values())

        