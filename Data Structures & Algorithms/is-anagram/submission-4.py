class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.makeHash(s) == self.makeHash(t)

    def makeHash(self, string) -> dict:
        counts = {}
        for char in string:
            if char not in counts:
                counts[char] = 0
            counts[char] += 1
        
        return counts