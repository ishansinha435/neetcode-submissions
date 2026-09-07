# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hmap = {n : i for i, n in enumerate(inorder)}
        pre_idx = 0

        def dfs(l, r):
            if l > r:
                return None
            nonlocal pre_idx
            root_val = preorder[pre_idx]
            pre_idx += 1
            m = hmap[root_val]
            return TreeNode(root_val, dfs(l, m - 1), dfs(m + 1, r))
        
        return dfs(0, len(inorder) - 1)