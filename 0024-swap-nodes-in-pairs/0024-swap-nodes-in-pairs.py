# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        H = ListNode(next=head)
        cur = H
        while cur.next and cur.next.next:
            first, second = cur.next, cur.next.next
            temp = second.next
            cur.next, second.next, first.next = second, first, temp
            cur = first
        return H.next