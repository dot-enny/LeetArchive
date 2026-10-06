# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if not root: return 0
        l_count, r_count = 1, 1
        if root.left: l_count += self.maxDepth(root.left)
        if root.right: r_count += self.maxDepth(root.right)
        return max(l_count, r_count)
