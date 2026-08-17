# two pointer
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            left = i # odd
            right = i
            while 0 <= left and right < len(s) and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1

            left = i # even
            right = i + 1
            while 0 <= left and right < len(s) and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1

        return res