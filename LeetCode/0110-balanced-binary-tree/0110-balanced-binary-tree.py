# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        def dfs(root):
            if not root: return [True, 0]
            
            lb, lh = dfs(root.left)
            rb, rh = dfs(root.right)

            balanced = (lb and rb) and (abs(lh - rh) <= 1)

            return [balanced, 1 + max(lh, rh)]

        return dfs(root)[0]