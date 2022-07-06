class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self._head = Node(0)
        self._count = 0

    def get(self, index: int) -> int:
        if 0 <= index < self._count:
            cur = self._head
            for _ in range(index+1):
                cur = cur.next
            return cur.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self._count, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            index = 0
        elif index > self._count:
            return
        self._count += 1
        prev, curr = None, self._head
        for _ in range(index+1):
            prev, curr = curr, curr.next
        add = Node(val)
        prev.next, add.next = add, curr

    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index < self._count:
            self._count -= 1
            prev, curr = None, self._head
            for _ in range(index+1):
                prev, curr = curr, curr.next
            prev.next = curr.next 


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)