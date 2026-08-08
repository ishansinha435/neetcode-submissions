# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q, res = deque(), []
        q.append((root, 0))
        while q:
            node, idx = q.popleft()
            if idx + 1 > len(res):
                res.append([])
            res[idx].append(node.val)
            if node.left:
                q.append((node.left, idx + 1))
            if node.right:
                q.append((node.right, idx + 1))
        return res
