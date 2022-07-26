# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        level = [root]
        while root and level:
            curmax = -inf
            newlevel = []
            for rt in level:
                curmax = max(curmax, rt.val)
                if rt.left:
                    newlevel.append(rt.left)
                if rt.right:
                    newlevel.append(rt.right)
            res.append(curmax)
            level = newlevel
        return res