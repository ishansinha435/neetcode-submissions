# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = False
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            valC = 1 if carry else 0
            carry = False
            curr_sum = val1 + val2 + valC
            if curr_sum > 9:
                carry = True
            curr.next = ListNode(curr_sum % 10)
            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return dummy.next

