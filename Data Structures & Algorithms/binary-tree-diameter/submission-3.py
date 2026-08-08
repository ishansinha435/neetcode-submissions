# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ldepth = self.maxDepth(root.left) if root.left else 0
        rdepth = self.maxDepth(root.right) if root.right else 0
        res = max(ldepth + rdepth, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        return res

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) if root else 0