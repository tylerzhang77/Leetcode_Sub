# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # recursive solution 
        res=[]
        self.helper(root,res)
        return res
    def helper(self,root,res):
        if root:
            res.append(root.val)
            self.helper(root.left, res)
            self.helper(root.right,res)
            