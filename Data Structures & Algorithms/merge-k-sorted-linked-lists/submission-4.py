# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = []
        for i in range(0, len(lists), 2):
            if i + 1 < len(lists):
                res.append(self.merge(lists[i], lists[i + 1]))
            else:
                res.append(lists[i])
        while len(res) > 1:
            merged = []
            for i in range(0, len(res), 2):
                if i + 1 < len(res):
                    merged.append(self.merge(res[i], res[i + 1]))
                else:
                    merged.append(res[i])
            res = merged
        return res[0] if len(res) > 0 else None

    def merge(self, l1, l2):
        dummy = curr = ListNode()
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return dummy.next
        