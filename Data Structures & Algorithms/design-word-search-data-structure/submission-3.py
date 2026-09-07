class TrieNode:
    
    def __init__(self):
        self.end = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True

    def search(self, word: str) -> bool:

        def dfs(i, node):
            if i == len(word):
                return node.end
            c = word[i]
            if c == ".":
                return any(dfs(i + 1, node) for node in node.children.values())
            elif c not in node.children:
                return False
            else:
                return dfs(i + 1, node.children[c])

        return dfs(0, self.root)
