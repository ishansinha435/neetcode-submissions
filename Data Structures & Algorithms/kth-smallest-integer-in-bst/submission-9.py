# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:   
        res, level = 0, 0

        def dfs(node):
            nonlocal level, res
            if node.left:
                dfs(node.left)
            level += 1
            if level == k:
                res = node.val
            if node.right:
                dfs(node.right)
        
        dfs(root)
        return res
