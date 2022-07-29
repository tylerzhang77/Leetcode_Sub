# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        res = 0
        while root and stack:
            rt = stack.pop()
            if rt.left and not rt.left.left and not rt.left.right:
                res += rt.left.val
            if rt.left:
                stack.append(rt.left)
            if rt.right:
                stack.append(rt.right)
        return res