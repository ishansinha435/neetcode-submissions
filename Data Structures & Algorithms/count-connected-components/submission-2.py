class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        hmap = defaultdict(list)
        for n1, n2 in edges:
            hmap[n1].append(n2)
            hmap[n2].append(n1)
        visited = set()
        
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in hmap[node]:
                dfs(neighbor)

        res = 0
        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i)
        return res
                