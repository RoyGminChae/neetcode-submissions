class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = dict()

        def opt(i, j): # longest common sub from 0 to i and 0 to j
            if i < 0 or j < 0:
                return 0

            if (i, j) in dp:
                return dp[(i, j)]

            if text1[i] == text2[j]:
                dp[(i, j)] = opt(i - 1, j - 1) + 1
            else:
                dp[(i, j)] = max(opt(i - 1, j), opt(i, j - 1))   

            return dp[(i, j)]     

        return opt(n - 1, m - 1)     

