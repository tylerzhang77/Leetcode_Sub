# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        cur = root
        parent = None
        
        while cur:
            if cur.val > val:
                parent = cur
                cur = cur.left
            else:
                parent = cur
                cur = cur.right
        
        if parent.val > val:
            parent.left = TreeNode(val)
        else:
            parent.right = TreeNode(val)
        
        return root