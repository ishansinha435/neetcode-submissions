# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque()
        if root: q.append([root, 0])
        while q:
            r, d = q.popleft()
            if d < len(res): res[d] = r.val
            else: res.append(r.val)
            if r.left: q.append([r.left, d + 1])
            if r.right: q.append([r.right, d + 1])
        return res
        