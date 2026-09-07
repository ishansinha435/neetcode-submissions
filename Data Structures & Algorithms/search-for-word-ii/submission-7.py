class TrieNode:
    def __init__(self):
        self.word = None
        self.children = {}
    
    def insert(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        root = TrieNode()
        for word in words:
            root.insert(word)
        visited = set()
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        R, C = len(board), len(board[0])

        def in_bounds(r, c):
            return 0 <= r < R and 0 <= c < C
        
        def dfs(r, c, node):
            if not in_bounds(r, c) or (r, c) in visited or board[r][c] not in node.children:
                return 
            node = node.children[board[r][c]]
            visited.add((r, c))
            if node.word:
                res.append(node.word)
                node.word = None
            for dr, dc in dirs:
                dfs(r + dr, c + dc, node)
            visited.remove((r, c))

        for r in range(R):
            for c in range(C):
                dfs(r, c, root)
        return res
        