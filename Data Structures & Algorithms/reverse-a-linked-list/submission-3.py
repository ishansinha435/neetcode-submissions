# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head and head.next:
            curr = head
            head = curr.next
            curr.next = prev
            prev = curr
        if head: head.next = prev
        return head