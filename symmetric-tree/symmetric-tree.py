# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return not root or self.helper(root.left, root.right)
    def helper(self, left, right):
        if not left and not right:
            return True
        if left and right and left.val == right.val:
            return self.helper(left.left,right.right) and self.helper(left.right, right.left)
        return False
