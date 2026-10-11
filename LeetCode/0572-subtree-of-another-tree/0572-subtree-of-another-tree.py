# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        stack = []
        curr = root
        while curr or stack:
            while curr:
                if self.sameTree(curr, subRoot): return True
                stack.append(curr)
                curr = curr.left
            curr = stack.pop().right
        
        return False


    def sameTree(self, node1, node2):
        if not node1 and not node2: return True
        if (not node1 or not node2) or (node1.val != node2.val): return False

        return self.sameTree(node1.left, node2.left) and self.sameTree(node1.right, node2.right)