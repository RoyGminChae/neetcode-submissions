class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dups = set()
        longest = 0
        i = 0
        j = 0
        
        while j < len(s):
            char = s[j]
            if s[j] in dups:
                while s[i] != char:
                    dups.remove(s[i])
                    i += 1
                i += 1

            dups.add(char)    
            longest = max(longest, j - i + 1)
            j += 1

        return longest


