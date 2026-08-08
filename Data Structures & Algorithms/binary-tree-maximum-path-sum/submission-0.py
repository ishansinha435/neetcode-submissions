# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val
        def dfs(node):
            if not node:
                return 0
            max_l, max_r = max(0, dfs(node.left)), max(0, dfs(node.right))
            self.res = max(self.res, node.val + max_l + max_r)
            return node.val + max(max_l, max_r)
        dfs(root)
        return self.res