class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = dict()
        for string in strs:
            anagram = "".join(sorted(string))
            # in uses equality check
            if anagram not in anagramDict:
                anagramDict[anagram] = list()
            
            anagramDict[anagram].append(string)
        
        output = []
        for anagram in anagramDict.keys():
            anagramList = list(anagramDict[anagram])
            output.append(anagramList)
            
        return output
        