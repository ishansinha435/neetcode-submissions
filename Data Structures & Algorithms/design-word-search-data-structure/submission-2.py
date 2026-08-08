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

        def dfs(node, idx):
            if idx == len(word):
                return node.word
            if word[idx] == ".":
                for c in node.children:
                    if dfs(node.children[c], idx + 1):
                        return True
                return False
            else:
                if word[idx] in node.children:
                    return dfs(node.children[word[idx]], idx + 1)
                return False

        return dfs(self.root, 0)