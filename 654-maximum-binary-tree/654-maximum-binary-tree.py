# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        rt = max(nums)
        rtind = nums.index(rt)
        root = TreeNode(rt)
        
        lt = nums[:rtind]
        rt = nums[rtind+1:]
        
        root.left = self.constructMaximumBinaryTree(lt)
        root.right = self.constructMaximumBinaryTree(rt)
        
        return root