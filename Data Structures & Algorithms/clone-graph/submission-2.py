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
            hmap[node] = Node(node.val)
            for neighbor in node.neighbors:
                if neighbor in hmap:
                    hmap[node].neighbors.append(hmap[neighbor])
                else:
                    hmap[node].neighbors.append(dfs(neighbor))
            return hmap[node]
        return dfs(node)