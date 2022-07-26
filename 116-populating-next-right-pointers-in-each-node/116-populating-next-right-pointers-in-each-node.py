"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root): 
        queue = [root]
        while queue and root:
            n = len(queue)
            for i in range(n):
                rt = queue.pop(0)
                if rt.left:
                    queue.append(rt.left)
                if rt.right:
                    queue.append(rt.right)
                if i == n-1:
                    break
                rt.next = queue[0]
        return root