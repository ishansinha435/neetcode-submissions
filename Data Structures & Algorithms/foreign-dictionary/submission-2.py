class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c : set() for w in words for c in w}
        for i in range(1, len(words)):
            w1, w2 = words[i - 1], words[i]
            c_idx = 0
            while c_idx != len(w1) and c_idx != len(w2) and w1[c_idx] == w2[c_idx]:
                c_idx += 1
            if c_idx == len(w2) and c_idx != len(w1):
                return ""
            elif c_idx == len(w1):
                continue
            adj[w1[c_idx]].add(w2[c_idx])

        visited = {}
        res = []

        def dfs(char):
            if char in visited:
                return not visited[char]
            visited[char] = True
            children = True
            for nei in adj[char]:
                if not dfs(nei):
                    children = False
            res.append(char)
            visited[char] = False
            return children

        for c in adj:
            if not dfs(c):
                return ""
        res.reverse()
        return "".join(res)
