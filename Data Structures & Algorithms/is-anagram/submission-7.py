class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(s):
            return False
        return self.makeHash(s) == self.makeHash(t)

    def makeHash(self, string) -> dict:
        counts = {}
        for char in string:
            if char not in counts:
                counts[char] = 0
            counts[char] += 1
        
        return counts