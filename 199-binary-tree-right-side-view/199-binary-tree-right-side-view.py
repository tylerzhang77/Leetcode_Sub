# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = [root]
        while root and stack:
            cur = []
            newlevel = []
            for rt in stack:
                cur.append(rt.val)
                if rt.left:
                    newlevel.append(rt.left)
                if rt.right:
                    newlevel.append(rt.right)
            res.append(cur[-1])
            stack = newlevel
        return res