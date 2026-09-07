"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hmap = {None:None}

        def dfs(node):
            if not node:
                return None
            copy = Node(node.val)
            hmap[node] = copy
            for neighbor in node.neighbors:
                if neighbor not in hmap:
                    dfs(neighbor)
                copy.neighbors.append(hmap[neighbor])

        dfs(node)
        return hmap[node]
        