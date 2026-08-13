class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
    
        res = []

        def dfs(i, path, total):
            # must come first before out of bounds
            if total == target:
                res.append(path[:])
                return 
            
            if i >= len(candidates):
                return

            val = candidates[i]
            if total + val > target:
                return

            path.append(val)
            dfs(i + 1, path, total + val)
            path.pop()
          
            # not include
            while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                i += 1
            
            # next i is not same or out of bound
            dfs(i + 1, path, total)
        
        dfs(0, [], 0)
        return res
            
            
            
        
            

            


            

