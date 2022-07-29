# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        level = [(root, root.val, [root.val])]
        res = []
        while level:
            rt, val, path = level.pop()
            if not rt.left and not rt.right and val == targetSum:
                res.append(path)
            if rt.left:
                level.append((rt.left, rt.left.val+val, path+[rt.left.val]))
            if rt.right:
                level.append((rt.right, rt.right.val+val, path+[rt.right.val]))        
        return res