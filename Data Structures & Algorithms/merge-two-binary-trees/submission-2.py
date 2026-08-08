# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        r1, r2 = root1, root2
        if not r1 and not r2:
            return None
        elif not r1:
            return r2
        else: 
            r1l = r1.left if r1 else None
            r2l = r2.left if r2 else None
            r1r = r1.right if r1 else None
            r2r = r2.right if r2 else None
            r1.val += (r2.val if r2 else 0)
            r1.left = self.mergeTrees(r1l, r2l)
            r1.right = self.mergeTrees(r1r, r2r)
            return r1