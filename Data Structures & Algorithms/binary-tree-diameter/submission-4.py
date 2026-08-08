# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node):
            nonlocal res
            if not node:
                return -1
            max_l, max_r = 1 + dfs(node.left), 1 + dfs(node.right)
            res = max(res, max_l + max_r)
            return max(max_l, max_r)
        dfs(root)
        return res
