class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)
        
        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei in adj[node]:
                dfs(nei)
            
        count = 0
        for node in range(n):
            if node not in adj:
                count += 1
            elif node not in visited:
                count += 1
                dfs(node)
        return count