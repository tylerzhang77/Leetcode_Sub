# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def rec(node):
            nonlocal ans
            if node:
                if low <= node.val <= high:
                    ans += node.val
                if low < node.val:
                    rec(node.left)
                if node.val < high:
                    rec(node.right)
        ans = 0
        rec(root)
        return ans