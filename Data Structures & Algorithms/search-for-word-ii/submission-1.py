class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add_word(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True
    
    def is_word(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.word

    def starts_with(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        R, C = len(board), len(board[0])
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        visited = set()
        res = set()

        trie = Trie()
        for w in words:
            trie.add_word(w)

        def in_bounds(r, c):
            return 0 <= r < R and 0 <= c < C
        
        def dfs(curr_pre, r, c):
            if not in_bounds(r, c) or (r, c) in visited:
                return

            curr_pre += board[r][c]
            if not trie.starts_with(curr_pre):
                return
            visited.add((r, c))
            if trie.is_word(curr_pre):
                res.add(curr_pre)  
            for dr, dc in dirs:
                dfs(curr_pre, r + dr, c + dc)
            visited.remove((r, c))
        
        for r in range(R):
            for c in range(C):
                dfs("", r, c)
        return list(res)