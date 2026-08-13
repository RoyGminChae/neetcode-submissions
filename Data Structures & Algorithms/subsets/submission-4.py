class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(path, i):
            res.append(path[:])
            for j in range(i, len(nums)):
                # After choosing nums[j], future choices must come after index j.
                path.append(nums[j])
                backtrack(path, j + 1)
                path.pop()

        backtrack([], 0)

        return res
                        
        

            