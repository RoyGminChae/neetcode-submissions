from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        left = 0
        right = 0

        window = Counter()
        tCounter = Counter(t) 

        found = 0
        need = len(t)

        minLength = float("inf")
        res = [-1, -1]

        while right < len(s):
            # maintain the found whenever right is added
            if s[right] in tCounter and window[s[right]] < tCounter[s[right]]:
                found += 1
            window[s[right]] += 1
        
            while (
                left <= right and
                (s[left] not in tCounter or
                 window[s[left]] > tCounter[s[left]])
            ):
                window[s[left]] -= 1
                left += 1

            length = right - left + 1
            if found == need and length < minLength:
                minLength = length
                res[0] = left
                res[1] = right
           
            right += 1

        if minLength == float("inf"):
            return ""
        
        return s[res[0]:res[1] + 1]


