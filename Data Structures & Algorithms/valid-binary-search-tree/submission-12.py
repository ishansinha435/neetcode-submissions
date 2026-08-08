# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def valid(node, l_bound, r_bound):
            if not node:
                return True
            return (l_bound < node.val < r_bound and
                    valid(node.left, l_bound, node.val) and
                    valid(node.right, node.val, r_bound))

        return valid(root, float('-inf'), float('inf'))
        
        
    