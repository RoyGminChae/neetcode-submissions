class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        dp = dict()

        def opt(i, j):
            if i >= n: 
                return m - j
                
            if j >= m:
                return n - i

            if (i, j) in dp:
                return dp[(i, j)]

            if word1[i] == word2[j]:
                # same
                dp[(i, j)] = opt(i + 1, j + 1)
            else: 
                dp[(i, j)] = 1 + min(
                    opt(i + 1, j), # delete
                    opt(i, j + 1), # insert
                    opt(i + 1, j + 1) # replace
                )

            return dp[(i, j)]

        return opt(0, 0)
            