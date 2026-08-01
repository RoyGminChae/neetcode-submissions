class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(path, i):
            res.append(path[:])
            for j in range(i, len(nums)):
                backtrack(path[:] + [nums[j]], j + 1)

        backtrack([], 0)

        return res
                        
        

            