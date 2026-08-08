# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None

        newHead = ListNode(head.val, None)
        head = head.next

        while head:
            newNode = ListNode(head.val, newHead)
            newHead = newNode
            head = head.next
        
        return newHead

            