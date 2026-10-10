# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        stack = []
        curr1, curr2 = p, q
        while curr1 or curr2 or stack:
            while curr1 and curr2:
                if curr1.val == curr2.val:
                    stack.append((curr1, curr2))
                    curr1 = curr1.left
                    curr2 = curr2.left
                else: return False
            if curr1 or curr2: return False
            curr = stack.pop()
            curr1 = curr[0].right
            curr2 = curr[1].right
        
        return True