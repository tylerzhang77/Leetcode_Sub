# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        level = [root]
        while root and level:
            newlevel = []
            cursum = 0
            lgt = 0
            for rt in level:
                cursum += rt.val
                lgt += 1
                if rt.left:
                    newlevel.append(rt.left)
                if rt.right:
                    newlevel.append(rt.right)
            res.append(cursum/lgt)
            level = newlevel
        return res