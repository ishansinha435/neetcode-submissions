# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        q = deque([root])
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if not node:
                    res.append("#")
                else:
                    res.append(f"{node.val}")
                    q.append(node.left)
                    q.append(node.right)
        return ("$".join(res))
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split("$")
        if data[0] == "#":
            return None
        root = TreeNode(int(data[0]))
        q = deque([root])
        idx = 1
        while q and idx < len(data):
            node = q.popleft()
            if data[idx] != "#":
                left = TreeNode(int(data[idx]))
                node.left = left
                q.append(left)
            idx += 1
            if data[idx] != "#":
                right = TreeNode(int(data[idx]))
                node.right = right
                q.append(right)
            idx += 1
        return root