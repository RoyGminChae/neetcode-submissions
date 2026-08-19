class Solution:
    # opt(i): word 0 to i can be segmented
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = dict()

        def opt(i):
            if i < 0:
                return True

            if i in dp:
                return dp[i]
            
            for word in wordDict:
                prevIndex = i - len(word)
                if s[prevIndex + 1: i + 1] == word and opt(prevIndex):
                    dp[i] = True
                    return dp[i]

            dp[i] = False
            return dp[i]

        return opt(n - 1)