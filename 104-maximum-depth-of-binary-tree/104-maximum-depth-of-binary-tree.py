# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        level = [root]
        res = 0
        while root and level:
            newlevel = []
            for rt in level:
                if rt.left:
                    newlevel.append(rt.left)
                if rt.right:
                    newlevel.append(rt.right)
            level = newlevel
            res += 1
        return res