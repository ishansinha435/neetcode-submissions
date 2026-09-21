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

        def build(l, r):
            nonlocal pre_idx
            if l > r:
                return None
            val = preorder[pre_idx]
            root = TreeNode(val)
            pre_idx += 1
            m = hmap[val]
            root.left = build(l, m - 1)
            root.right = build(m + 1, r)
            return root
        
        return build(0, len(preorder) - 1)