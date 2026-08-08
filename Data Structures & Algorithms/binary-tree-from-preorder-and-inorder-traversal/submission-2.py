# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        m = 0
        while m < len(preorder) and inorder[m] != preorder[0]:
            m += 1
        root.left = self.buildTree(preorder[1:m+1], inorder[:m])
        root.right = self.buildTree(preorder[m+1:], inorder[m+1:])
        return root
        