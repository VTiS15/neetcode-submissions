class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = self.right = None


class TreeMap:
    
    def __init__(self):
        self.mapping = {}
        self.root = None

    def insert(self, key: int, val: int) -> None:
        if key not in self.mapping:
            node = Node(key, val)

            if self.root:
                prev, curr = None, self.root
                while curr:
                    prev = curr
                    if key < curr.key:
                        curr = curr.left
                    else:
                        curr = curr.right

                if key < prev.key:
                    prev.left = node
                else:
                    prev.right = node
            else:
                self.root = node

        self.mapping[key] = val

    def get(self, key: int) -> int:
        return self.mapping.get(key, -1)

    def getMin(self) -> int:
        curr = self.root
        if not curr:
            return -1

        while curr.left:
            curr = curr.left
        return curr.value

    def getMax(self) -> int:
        curr = self.root
        if not curr:
            return -1

        while curr.right:
            curr = curr.right
        return curr.value

    def remove(self, key: int) -> None:
        if key not in self.mapping:
            return

        del self.mapping[key]

        prev, curr = None, self.root
        while curr.key != key:
            prev = curr
            if key < curr.key:
                curr = curr.left
            else:
                curr = curr.right
        
        if curr.left and curr.right:
            prev_repl, repl = None, curr.right
            while repl.left:
                prev_repl = repl
                repl = repl.left
            if prev_repl:
                curr.key = repl.key
                prev_repl.left = None
            else:
                curr.key = repl.key
                curr.right = None

        elif curr.left or curr.right:
            child = curr.left if curr.left else curr.right
            if prev:
                if curr == prev.left:
                    prev.left = child
                else:
                    prev.right = child
            else:
                self.root = child

        else:
            if prev:
                if prev.left == curr:
                    prev.left = None
                else:
                    prev.right = None
            else:
                self.root = None

    def getInorderKeys(self) -> List[int]:
        result = []
        stack = []
        curr = self.root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            result.append(curr.key)
            curr = curr.right
        
        return result
