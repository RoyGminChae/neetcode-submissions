from collections import deque

# bfs
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 0

        n = len(beginWord)
        wordSet = set(wordList)

        letters = set("abcdefghijklmnopqrstuvwxyz")
        res = {beginWord: 1}
        parents = {beginWord: None}
        visited = set()

        queue = deque()
        queue.append(beginWord) 
        while queue:
            word = queue.popleft()
            
            for i in range(n):
                for letter in letters - set([word[i]]):
                    nextWord = word[:i] + letter + word[i + 1:]

                    if nextWord not in wordSet:
                        continue

                    if nextWord in visited:
                        continue

                    if nextWord == parents[word]:
                        continue
                    
                    if nextWord == endWord:
                        return res[word] + 1

                    visited.add(nextWord)
                    parents[nextWord] = word
                    res[nextWord] = res[word] + 1
                    queue.append(nextWord)

        return 0
                    
