# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: TreeNode | None, target: int) -> TreeNode | None:
        def dfs(root):
            if not root: return (root, False)

            left = dfs(root.left)
            right = dfs(root.right)

            if left[1]: root.left = None
            if right[1]: root.right = None

            if not root.left and not root.right and root.val == target: return (None, True)
            else: return (root, False)

        return dfs(root)[0]
