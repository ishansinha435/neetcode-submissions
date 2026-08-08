# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev = dummy = ListNode(0, head)
        curr = head
        while curr:
            while curr and curr.val == val:
                curr = curr.next
            prev.next = curr
            prev = curr
            curr = curr.next if curr else None
        return dummy.next