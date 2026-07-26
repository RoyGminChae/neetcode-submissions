class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i, jump in enumerate(nums):
            if farthest < i:
                return False

            farthest = max(farthest, i + jump)

        return True        





        # dp works, but it's O(n^2)
        # dp = dict()

        # def opt(i):
        #     if i >= len(nums) - 1:
        #         return True

        #     if i in dp:
        #         return dp[i]
            
        #     for j in range(1, nums[i] + 1):
        #         if opt(i + j):
        #             dp[i] = True
        #             return True

        #     dp[i] = False
        #     return False

        # return opt(0)