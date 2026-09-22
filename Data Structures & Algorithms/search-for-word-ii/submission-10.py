class TrieNode:

    def __init__(self):
        self.end = None
        self.children = {}

    def add(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        R, C = len(board), len(board[0])
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        visited = set()
        res = set()
        root = TrieNode()
        for word in words:
            root.add(word)

        def in_bounds(r, c):
            return 0 <= r < R and 0 <= c < C
        
        def dfs(r, c, node):
            if node.end:
                res.add(node.end)
            if not in_bounds(r, c) or (r, c) in visited or board[r][c] not in node.children:
                return
            visited.add((r, c))
            for dr, dc in dirs:
                dfs(r + dr, c + dc, node.children[board[r][c]])
            visited.remove((r, c))   

        for r in range(R):
            for c in range(C):
                dfs(r, c, root)
        return list(res)