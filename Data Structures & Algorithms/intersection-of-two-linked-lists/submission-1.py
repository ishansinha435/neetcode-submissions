# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a, b = headA, headB
        while a.next and b.next:
            if a == b:
                return a
            a, b = a.next, b.next
        skipA, skipB = 0, 0
        if not a.next:
            while b.next:
                b = b.next
                skipB += 1
        elif not b.next:
            while a.next:
                a = a.next
                skipA += 1
        if a != b:
            return None
        a, b = headA, headB
        while skipA:
            a = a.next
            skipA -= 1
        while skipB:
            b = b.next
            skipB -= 1
        while True:
            if a == b:
                return a
            a, b = a.next, b.next