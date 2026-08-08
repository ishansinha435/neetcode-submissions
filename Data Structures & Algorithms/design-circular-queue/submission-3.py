class Node:

    def __init__(self, val=0, nxt=None, prev=None):
        self.val = val
        self.nxt = nxt
        self.prev = prev

class MyCircularQueue:

    def __init__(self, k: int):
        self.front = Node()
        self.tail = Node(0, None, self.front)
        self.front.nxt = self.tail
        self.space = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        new_node = Node(value, self.tail, self.tail.prev)
        self.tail.prev.nxt = new_node
        self.tail.prev = new_node
        self.space -= 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front.nxt = self.front.nxt.nxt
        self.front.nxt.prev = self.front
        self.space += 1
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.front.nxt.val

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.tail.prev.val

    def isEmpty(self) -> bool:
        return self.front.nxt == self.tail

    def isFull(self) -> bool:
        return self.space == 0
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()