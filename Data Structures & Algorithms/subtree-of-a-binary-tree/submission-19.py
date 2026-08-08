# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        ser_root = self.serialize(root)
        ser_sub = self.serialize(subRoot)
        return ser_sub in ser_root
    
    def serialize(self, tree):
        if not tree:
            return "$#"
        return f"${self.serialize(tree.left)}{tree.val}{self.serialize(tree.right)}"
        