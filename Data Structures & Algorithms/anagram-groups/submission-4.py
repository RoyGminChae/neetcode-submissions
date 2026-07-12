class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for string in strs:
            anagram = tuple(sorted(string))
            if anagram not in anagrams:
                anagrams[anagram] = []
            anagrams[anagram].append(string)

        output = []
        for anagram in anagrams:
            output.append(anagrams[anagram])
        
        return output