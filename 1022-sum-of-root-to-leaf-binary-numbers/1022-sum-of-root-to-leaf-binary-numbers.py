# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def getbin(root, res):
            if root is None: return 0
            res = (2 * res)  + root.val
            if root.left is None and root.right is None:
                return res
            return getbin(root.left, res) + getbin(root.right, res)
        return getbin(root, 0)
