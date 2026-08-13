class Solution:
    # for loop version variant
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(path, i, total):
            if total == target:
                res.append(path)
                return

            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    continue
                    
                backtrack(path[:] + [nums[j]], j, total + nums[j])

        backtrack([], 0, 0)

        return res
