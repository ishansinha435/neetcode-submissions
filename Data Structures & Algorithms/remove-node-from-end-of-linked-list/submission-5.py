# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length, node = 0, head
        while node:
            length, node = length + 1, node.next
        index, node = length - n, head
        if index == 0: return head.next
        for i in range(index - 1):
            node = node.next
        node.next = node.next.next
        return head

        