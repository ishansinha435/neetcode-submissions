# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # curr = head
        # while curr:
        #     curr.val = -1001
        #     if curr.next and curr.next.val == -1001:
        #         return True
        #     curr = curr.next
        # return False
        fast = slow = head
        while fast and slow:
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                return False
            if slow == fast:
                return True
        return False