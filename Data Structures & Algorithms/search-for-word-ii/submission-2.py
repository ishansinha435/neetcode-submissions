class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

    def add_word(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        R, C = len(board), len(board[0])
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        visited = set()
        res = set()

        root = TrieNode()
        for w in words:
            root.add_word(w)

        def in_bounds(r, c):
            return 0 <= r < R and 0 <= c < C
        
        def dfs(curr_pre, r, c, node):
            if not in_bounds(r, c) or (r, c) in visited or board[r][c] not in node.children:
                return

            visited.add((r, c))
            node = node.children[board[r][c]]
            curr_pre += board[r][c]
            if node.word:
                res.add(curr_pre)  
            for dr, dc in dirs:
                dfs(curr_pre, r + dr, c + dc, node)
            visited.remove((r, c))
        
        for r in range(R):
            for c in range(C):
                dfs("", r, c, root)
        return list(res)