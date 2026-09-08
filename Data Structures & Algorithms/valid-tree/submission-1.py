class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        hmap = defaultdict(list)
        visited = set()
        for n1, n2 in edges:
            hmap[n1].append(n2)
            hmap[n2].append(n1)
        
        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            return all(dfs(neighbor, node) for neighbor in hmap[node] if neighbor != parent)
        
        if not dfs(0, None):
            return False
        return len(visited) == n
