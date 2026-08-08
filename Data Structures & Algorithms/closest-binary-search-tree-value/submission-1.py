# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        res, min_diff = root.val, float('inf')

        def dfs(node):
            nonlocal res, min_diff
            if not node:
                return
            if abs(node.val - target) < min_diff:
                res, min_diff = node.val, abs(node.val - target)
            if node.val < target:
                dfs(node.right)
            else:
                dfs(node.left)
        
        dfs(root)
        return res