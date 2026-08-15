class Solution: 
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def isPali(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False

                left += 1
                right -= 1

            return True
        
        def dfs(i):
            if i >= len(s):
                res.append(part[:])
                return 

            for j in range(i, len(s)):            
                if not isPali(i, j):
                    continue

                part.append(s[i:j + 1])
                dfs(j + 1)
                part.pop()

        dfs(0)
        return res                    




        




