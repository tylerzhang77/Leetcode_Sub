# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return []
        stack = []  
        result = []
        res = inf
        cur = root
        while cur or stack:
            if cur:     
                stack.append(cur)
                cur = cur.left		            
            else:		
                cur = stack.pop()
                result.append(cur.val)
                if len(result) > 1:
                    
                    res = min(result[-1] - result[-2], res)
                cur = cur.right	
        return res
        