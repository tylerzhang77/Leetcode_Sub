# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        H = ListNode(next = head)
        prev = H
        while prev.next and prev.next.next:
            curr = prev.next
            post = prev.next.next
            curr.next, post.next, prev.next = post.next, curr, post
            prev = prev.next.next
        return H.next