class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanedList = list(filter(lambda c: c.isalnum(), s.lower()))
        i = 0
        j = len(cleanedList) - 1
        while i < j:
            if cleanedList[i] != cleanedList[j]:
                return False
            i += 1
            j -= 1
        
        return True
            
        