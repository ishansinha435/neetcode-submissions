# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        check = False
        res = ListNode()
        head = res
        while l1 or l2:
            sumNodes = 0
            if check:
                sumNodes = 1
                check = False

            if l1 and l2: 
                sumNodes += (l1.val + l2.val)
            elif l1:
                sumNodes += l1.val
            else: 
                sumNodes += l2.val

            if sumNodes >= 10:
                res.next = ListNode(sumNodes % 10, None)
                check = True
            else:
                res.next = ListNode(sumNodes, None)

            res = res.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if check:
            res.next = ListNode(1, None)
        return head.next
