class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {char: 0 for char in s}
        longest = 0
        l = 0
        r = 0
        
        maxf = 0
        while r < len(s):
            freq[s[r]] += 1 
            maxf = max(maxf, freq[s[r]])
            while (r - l + 1) - maxf > k:
                freq[s[l]] -= 1
                l += 1
                
            longest = max(longest, r - l + 1)
            r += 1
        
        return longest


                


            

