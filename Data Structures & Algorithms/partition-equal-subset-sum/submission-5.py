class Solution:
    # includion exclusion subset
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False

        dp = dict()

        def opt(i, target):
            if i < 0:
                return target == 0

            if target < 0:
                return False

            if (i, target) in dp:
                return dp[(i, target)]

            dp[(i, target)] = opt(i - 1, target - nums[i]) or opt(i - 1, target)
            return dp[(i, target)]

        return opt(len(nums) - 1, sum(nums) // 2)   


            

            
            
