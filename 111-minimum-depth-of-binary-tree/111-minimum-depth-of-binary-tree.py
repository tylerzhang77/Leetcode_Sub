# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        level = deque()
        level.append(root)
        res = 1
        while level:
            for i in range(len(level)):
                rt = level.popleft()
                if not rt.left and not rt.right:
                    return res
                if rt.left:
                    level.append(rt.left)
                if rt.right:
                    level.append(rt.right)
            res += 1
        return res