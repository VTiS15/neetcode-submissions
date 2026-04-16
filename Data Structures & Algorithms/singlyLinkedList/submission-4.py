class Node:
    def __init__(self, value, nxt = None):
        self.value = value
        self.nxt = nxt


class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        node = self.head
        for _ in range(index):
            if not node:
                return -1
            node = node.nxt

        if node:
            return node.value
        return -1

    def insertHead(self, val: int) -> None:
        self.head = Node(val, self.head)

    def insertTail(self, val: int) -> None:
        curr = self.head
        node = Node(val)
        if curr:
            while curr.nxt:
                curr = curr.nxt
            curr.nxt = node
        else:
            self.head = node

    def remove(self, index: int) -> bool:
        prev, curr = None, self.head
        if not curr:
            return False

        for _ in range(index):
            if not curr.nxt:
                return False
            prev, curr = curr, curr.nxt

        if prev:
            prev.nxt = curr.nxt
        else:
            self.head = curr.nxt
        return True

    def getValues(self) -> List[int]:
        node = self.head
        arr = []
        while node:
            arr.append(node.value)
            node = node.nxt
        return arr
