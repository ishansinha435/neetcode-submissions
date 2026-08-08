# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def helper(root, arr, level):
            if not root:
                return
            if level >= len(arr):
                arr.append([])
            arr[level].append(root.val)
            helper(root.left, arr, level + 1)
            helper(root.right, arr, level + 1)
        helper(root, res, 0)
        return res
        
        
        