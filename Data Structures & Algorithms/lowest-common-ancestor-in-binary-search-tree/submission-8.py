# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        while True:
            if p == root or q == root or min(p.val, q.val) < root.val and max(p.val, q.val) > root.val:
                return root
            if p.val < root.val:
                root = root.left
            else:
                root = root.right
            
        