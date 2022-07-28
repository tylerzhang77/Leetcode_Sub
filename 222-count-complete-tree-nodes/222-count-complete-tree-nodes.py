# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        level = deque()
        level.append(root)
        res = 0
        while root and level:
            sz = len(level)
            for _ in range(sz):
                res += 1
                rt = level.popleft()
                if rt.left:
                    level.append(rt.left)
                if rt.right:
                    level.append(rt.right)
        return res