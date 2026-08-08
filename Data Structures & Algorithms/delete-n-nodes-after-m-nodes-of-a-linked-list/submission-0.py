# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        curr = dummy = ListNode(0, head)
        while curr:
            for _ in range(m):
                curr = curr.next if curr else None
            nxt = curr.next if curr else None
            for _ in range(n):
                nxt = nxt.next if nxt else None
            if curr:
                curr.next = nxt
        return dummy.next