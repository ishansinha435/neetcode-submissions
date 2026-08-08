class TrieNode:

    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

    def search(self, word: str) -> bool:
        res = False

        def dfs(node, idx):
            nonlocal res
            if idx == len(word) and node.word:
                res = True
            if idx == len(word):
                return
            if word[idx] == ".":
                for c in node.children:
                    dfs(node.children[c], idx + 1)
            else:
                if word[idx] in node.children:
                    dfs(node.children[word[idx]], idx + 1)

        dfs(self.root, 0)
        return res
        