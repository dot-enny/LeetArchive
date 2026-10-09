# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        def dfs(curr, balanced):
            if not curr: return [0, balanced]

            lh, lb = dfs(curr.left, balanced)
            rh, rb = dfs(curr.right, balanced)

            if (not lb) or (not rb): 
                return [1 + max(lh, rh), False]

            if abs(lh - rh) > 1: 
                balanced = False

            val = [1 + max(lh, rh), balanced]
            return val

        is_balanced = dfs(root, True)[1]
        return is_balanced