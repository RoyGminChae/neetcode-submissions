class Solution:
    # inclusion exclusion decision tree
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i, path):
            if i >= len(nums):
                res.append(path)
                return

            backtrack(i + 1, path[:])
            backtrack(i + 1, path[:] + [nums[i]])

        backtrack(0, [])
        return res

            

