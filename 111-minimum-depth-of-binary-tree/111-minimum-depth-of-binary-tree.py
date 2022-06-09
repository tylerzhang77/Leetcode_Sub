# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            if not root.left or not root.right:
                return 1+max(self.minDepth(root.left),self.minDepth(root.right))
        else:
            return 0
        return 1+min(self.minDepth(root.left),self.minDepth(root.right))