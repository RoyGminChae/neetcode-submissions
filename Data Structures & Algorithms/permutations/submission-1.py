class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def dfs(path, picked): 
            if len(path) == len(nums):
                res.append(path[:])
                return

            for num in nums:
                if num in picked:
                    continue

                path.append(num)
                picked.add(num)
                dfs(path, picked)
                path.pop()
                picked.remove(num)

        dfs([], set())
        return res
            

                