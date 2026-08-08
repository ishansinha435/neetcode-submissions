# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        group_prev = dummy = ListNode(0, head)
        while True:
            kth = self.findKth(group_prev, k)
            if not kth:
                break
            group_next = kth.next
            curr, prev = group_prev.next, group_next
            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            temp = group_prev.next
            group_prev.next = kth
            group_prev = temp
        return dummy.next
    
    def findKth(self, node, k):
        while node and k > 0:
            node = node.next
            k -= 1
        return node