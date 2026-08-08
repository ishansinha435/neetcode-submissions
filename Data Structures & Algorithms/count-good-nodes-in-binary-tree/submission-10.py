# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(root, maxi):
            nonlocal res
            if not root:
                return
            if root.val >= maxi:
                res += 1
            maxi = max(maxi, root.val)
            dfs(root.left, maxi)
            dfs(root.right, maxi)
        dfs(root, float('-inf'))
        return res