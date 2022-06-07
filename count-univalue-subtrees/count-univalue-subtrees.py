# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        self.counter(root)
        return self.count
    
    def counter(self, node):
        if not node:
            return True
        L, R = self.counter(node.left), self.counter(node.right)
        if L and R and (not node.left or node.left.val == node.val) and (not node.right or node.right.val == node.val):
            self.count += 1
            return True
        return False
