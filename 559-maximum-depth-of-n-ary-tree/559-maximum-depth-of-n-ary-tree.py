"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        level = [root]
        res = 0
        while root and level:
            newlevel = []
            for rt in level:
                if rt.children:
                    newlevel.extend(rt.children)
            level = newlevel
            res += 1
        return res
        