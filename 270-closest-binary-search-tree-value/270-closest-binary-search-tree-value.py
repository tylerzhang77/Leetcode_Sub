# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        mindif = inf
        res = 0
        def helper(node):
            nonlocal mindif
            nonlocal res
            if node:
                if abs(node.val - target) < mindif:
                    mindif = abs(node.val - target)
                    res = node.val
                helper(node.left)
                helper(node.right)
        helper(root)
        return res
                
            