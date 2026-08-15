class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp = {}

        def opt(i, excludeFirst):
            if i < 0 or (i == 0 and excludeFirst):
                return 0

            if (i, excludeFirst) in dp:
                return dp[(i, excludeFirst)]

            dp[(i, excludeFirst)] = max(
                nums[i] + opt(i - 2, excludeFirst),
                opt(i - 1, excludeFirst)
            )

            return dp[(i, excludeFirst)]

        return max(
            opt(len(nums) - 1, True),   # exclude first → houses 1...n-1
            opt(len(nums) - 2, False)   # exclude last → houses 0...n-2
        )