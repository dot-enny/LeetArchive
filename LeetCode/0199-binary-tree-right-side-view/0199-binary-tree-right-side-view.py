# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if not root: return []
        
        res = [root.val]
        q = deque([root])
        
        while q:
            q_len = len(q)
            right = None
            for i in range(q_len):
                node = q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    right = node.left if node.left else right
                    right = node.right if node.right else right
            if right: res.append(right.val)
        
        return res