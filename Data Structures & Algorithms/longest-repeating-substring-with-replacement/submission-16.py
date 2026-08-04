from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = Counter()
        maxFreq = 0
        longest = 0


        left = 0
        right = 0
        while right < len(s):
            counter[s[right]] += 1
            maxFreq = max(maxFreq, counter[s[right]])
            while (right - left + 1) - maxFreq > k:
                counter[s[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)
            right += 1

        return longest

