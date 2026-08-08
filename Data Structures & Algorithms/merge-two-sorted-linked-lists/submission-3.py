# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1, l2 = list1, list2
        head = l1 
        if not l1 or l2 and l1.val > l2.val:
            head = l2
        while l1 and l2:
            if l1.val <= l2.val:
                while l1.next and l1.next.val <= l2.val:
                    l1 = l1.next
                temp = l1.next
                l1.next = l2
                l1 = temp
            else:
                while l2.next and l2.next.val <= l1.val:
                    l2 = l2.next
                temp = l2.next
                l2.next = l1
                l2 = temp
        return head