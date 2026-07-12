class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        charDict1 = dict()
        charDict2 = dict()
        for i in range(len(s)):
            char1 = s[i]
            char2 = t[i]

            if char1 not in charDict1.keys():
                charDict1[char1] = 0
            charDict1[char1] += 1

            if char2 not in charDict2.keys():
                charDict2[char2] = 0
            charDict2[char2] += 1

        if charDict1 != charDict2:
            return False
        else:
            return True
