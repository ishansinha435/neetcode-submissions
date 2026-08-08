"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hmap = {}      

        def dfs(curr):
            if curr in hmap:
                return hmap[curr]
            hmap[curr] = Node(curr.val)
            for n in curr.neighbors:
                hmap[curr].neighbors.append(dfs(n))
            return hmap[curr]
    
        return dfs(node) if node else None
        