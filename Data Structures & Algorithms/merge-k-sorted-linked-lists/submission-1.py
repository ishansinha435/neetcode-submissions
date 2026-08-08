# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        curr = dummy = ListNode(None)
        while True:
            min_i = -1
            for i, node in enumerate(lists):
                if not node:
                    continue
                if min_i == -1 or node.val < lists[min_i].val:
                    min_i = i
            if min_i == -1:
                break
            curr.next = lists[min_i]
            curr, lists[min_i] = curr.next, lists[min_i].next
        return dummy.next

