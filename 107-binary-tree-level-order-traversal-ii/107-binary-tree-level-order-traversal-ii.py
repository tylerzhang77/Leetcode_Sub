# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        level = [root]
        while root and level:
            newlevel = []
            cur = []
            for node in level:
                cur.append(node.val)
                if node.left:
                    newlevel.append(node.left)
                if node.right:
                    newlevel.append(node.right)
            res.append(cur)
            level = newlevel
        return res[::-1]