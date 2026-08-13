class Solution:
     # ")" can be used when leftUsed > rightdUsed
     # "("" can be used when leftUsed < n

    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(path, leftN, rightN):
            if leftN == rightN == n:
                res.append("".join(path[:]))
                return

            if leftN < n:
                path.append("(")
                dfs(path, leftN + 1, rightN)
                path.pop()

            if leftN > rightN:
                path.append(")")
                dfs(path, leftN, rightN + 1)
                path.pop()    

        dfs([], 0, 0)
        return res
       



    