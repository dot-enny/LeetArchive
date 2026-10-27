# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(prev, curr):
            if not curr: return 0
            
            p, res = prev, 0

            if prev.val <= curr.val: p, res = curr, 1
            
            res += dfs(p, curr.left) + dfs(p, curr.right)

            return res

        return 1 + dfs(root, root.left) + dfs(root, root.right)