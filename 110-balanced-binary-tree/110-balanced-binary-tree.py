# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return True if self.height(root) != -1 else False
    
    def height(self, root):
        if not root:
            return 0
        if (lt := self.height(root.left)) == -1:
            return -1
        if (rt := self.height(root.right)) == -1:
            return -1 
        if (abs(lt - rt)) > 1:
            return -1
        return 1 + max(lt, rt)
