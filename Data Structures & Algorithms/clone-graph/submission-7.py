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
        
        def dfs(node):
            if not node:
                return None
            if node not in hmap:
                hmap[node] = Node(node.val)
                for n in node.neighbors:
                    hmap[node].neighbors.append(dfs(n))
            return hmap[node]

        return dfs(node)
