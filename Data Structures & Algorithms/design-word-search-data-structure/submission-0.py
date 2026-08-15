class TrieNode:
    def __init__(self):
        self.children = dict()
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()

            curr = curr.children[char]
        
        curr.isWord = True
            

    def search(self, word: str) -> bool:
        
        def dfs(i, node):
            if i >= len(word):
                return node.isWord

            char = word[i]

            if char == ".":
                for nextNode in node.children.values():
                    if dfs(i + 1, nextNode):
                        return True
                
                return False

            else:
                if char not in node.children:
                    return False

                return dfs(i + 1, node.children[char])

        return dfs(0, self.root)


            
            

