from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)

        if n > m:
            return False

        counter = Counter(s1)

        for i in range(m - n + 1):
            j = i + n 
            temp = Counter(s2[i:j])
            if counter == temp:
                return True

        return False
