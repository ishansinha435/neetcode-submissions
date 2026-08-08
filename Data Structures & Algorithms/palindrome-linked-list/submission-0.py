# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
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
        while l and r:
            if l.val != r.val:
                return False
            l, r = l.next, r.next
        return True