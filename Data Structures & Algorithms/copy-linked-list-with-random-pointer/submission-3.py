"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr, hmap = head, defaultdict(lambda: Node(0))
        hmap[None] = None
        while curr:
            hmap[curr].val = curr.val
            hmap[curr].next = hmap[curr.next]
            hmap[curr].random = hmap[curr.random]
            curr = curr.next
        return hmap[head]
        
        