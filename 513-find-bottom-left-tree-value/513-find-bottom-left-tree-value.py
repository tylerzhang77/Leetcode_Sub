# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        level = deque()
        level.append(root)
        res = []
        
        while level:
            size = len(level)
            for i in range(size):
                rt = level.popleft()
                if i == 0:
                    res.append(rt.val)
                if rt.left:
                    level.append(rt.left)
                if rt.right:
                    level.append(rt.right)
        return res[-1]
            