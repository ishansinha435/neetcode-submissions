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
            if word[i] == ".":
                return any(dfs(i + 1, node.children[c]) for c in node.children)
            if word[i] not in node.children:
                return False
            return dfs(i + 1, node.children[word[i]])

        return dfs(0, self.root)
