# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        curr, prev = slow, None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        l, r = head, prev
        while r.next:
            temp = l.next
            l.next = r
            l = temp
            temp = r.next
            r.next = l
            r = temp