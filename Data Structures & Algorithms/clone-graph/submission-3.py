"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hmap, visited = {None:None}, set()

        if not node:
            return None
        hmap[node] = Node(node.val)

        def dfs(curr):
            for n in curr.neighbors:
                if n not in hmap:
                    hmap[n] = Node(n.val)
                    dfs(n) 
        dfs(node)
        
        def clone(curr):
            if curr not in visited:
                visited.add(curr)
                for n in curr.neighbors:
                    hmap[curr].neighbors.append(hmap[n])
                    clone(n)
        clone(node)
        return hmap[node]
                
        