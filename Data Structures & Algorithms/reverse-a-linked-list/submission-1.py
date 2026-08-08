# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head: return None
        mini, prev, curr = None, head, head.next

        while curr:
            prev.next = mini
            mini = prev
            prev = curr
            curr = curr.next
        
        prev.next = mini
        return prev