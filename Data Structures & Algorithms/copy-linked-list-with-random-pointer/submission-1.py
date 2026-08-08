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
        hmap, curr, = {}, head
        while curr:
            new_node = Node(curr.val)
            hmap[curr] = new_node
            curr = curr.next
        curr = head
        while curr:
            hmap[curr].next = hmap[curr.next] if curr.next else None
            hmap[curr].random = hmap[curr.random] if curr.random else None
            curr = curr.next
        return hmap[head] if head else None
        
        