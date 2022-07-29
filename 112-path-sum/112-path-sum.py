# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False 
        stack = [(root,root.val)]
        while stack:
            rt, val = stack.pop()
            if not rt.left and not rt.right and val == targetSum:
                return True
            if rt.left:
                stack.append((rt.left, rt.left.val + val))
            if rt.right:
                stack.append((rt.right, rt.right.val + val))
        return False
