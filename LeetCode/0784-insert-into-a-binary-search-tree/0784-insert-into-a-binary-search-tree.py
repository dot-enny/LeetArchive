# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        if not root: return TreeNode(val)
        
        prev, curr = root, root
        while curr:
            prev = curr
            if val < curr.val:
                curr = curr.left
            elif val > curr.val: curr = curr.right
        
        if (val < prev.val): prev.left = TreeNode(val)
        elif (val > prev.val): prev.right = TreeNode(val)

        return root