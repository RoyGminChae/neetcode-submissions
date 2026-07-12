class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for string in strs:
            anagram = tuple(sorted(string))
            if anagram not in anagrams:
                anagrams[anagram] = []
            anagrams[anagram].append(string)

        return list(anagrams.values())