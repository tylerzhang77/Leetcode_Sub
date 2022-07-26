"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        level = [root]
        while root and level:
            cur = []
            newlevel = []
            for rt in level:
                cur.append(rt.val)
                if rt.children:
                    newlevel.extend(rt.children)
            res.append(cur)
            level = newlevel
        return res