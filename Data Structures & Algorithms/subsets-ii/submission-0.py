# inclusion/exclusion
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(i, path):
            if i >= len(nums):
                res.append(path[:])
                return
            
            path.append(nums[i])
            dfs(i + 1, path)
            path.pop()

            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            
            # next i must be different or out of bounds
            dfs(i + 1, path)     

        dfs(0, [])
        return res