# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lists = deque(lists)
        while len(lists) > 1:
            lists.append(self.merge(lists.popleft(), lists.popleft()))
        return lists[0] if lists and lists[0] else None

    def merge(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1, l2 = list1, list2
        curr = tmp = ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return tmp.next