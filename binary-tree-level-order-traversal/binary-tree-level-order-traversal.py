# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res, level = [], [root]
        while root and level:
            curNode = []
            newlevel = []
            for node in level:
                curNode.append(node.val)
                if node.left:
                    newlevel.append(node.left)
                if node.right:
                    newlevel.append(node.right)
            res.append(curNode)
            level = newlevel
        return res