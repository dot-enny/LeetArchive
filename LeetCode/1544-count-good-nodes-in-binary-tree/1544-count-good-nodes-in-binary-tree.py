# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 1

        def dfs(prev, curr):
            if not curr: return
            if prev.val <= curr.val:
                self.res += 1
                dfs(curr, curr.left)
                dfs(curr, curr.right)
            else:
                dfs(prev, curr.left)
                dfs(prev, curr.right)

        dfs(root, root.left)
        dfs(root, root.right)

        return self.res