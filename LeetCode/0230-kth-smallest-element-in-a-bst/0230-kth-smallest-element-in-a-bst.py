# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        n, curr, stack = 1, root, []

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            next = stack.pop()
            curr = next.right
            if n < k: n += 1
            else: return next.val