class Solution:
    # index by index include/exclude version
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, path, total):
            if i >= len(nums) or total > target:
                return
            
            if total == target:
                res.append(path[:])
                return
            
            # include current i
            backtrack(i, path[:] + [nums[i]], total + nums[i])

            # exclude current i
            backtrack(i + 1, path[:], total)

        backtrack(0, [], 0)
        return res
