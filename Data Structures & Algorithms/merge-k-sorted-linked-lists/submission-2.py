# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def merge(l1, l2):
            curr = dummy = ListNode()
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

        while len(lists) > 1:
            merged_lists = []
            for i in range(1, len(lists), 2):
                merged_lists.append(merge(lists[i - 1], lists[i]))
            if len(lists) % 2 == 1:
                merged_lists.append(lists[-1])
            lists = merged_lists
        return lists[0]


