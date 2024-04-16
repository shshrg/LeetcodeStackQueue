from collections import deque

class MyQueue:

    def __init__(self):
        self.stack = deque()

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        new = deque()
        while not self.empty():
            new.append(self.stack.pop())
        res = new.pop()
        while len(new) != 0:
            self.push(new.pop())
        return res


    def peek(self) -> int:
        new = deque()
        while not self.empty():
            new.append(self.stack.pop())
        res = new.pop()
        self.stack.append(res)
        while len(new) != 0:
            self.stack.append(new.pop())
        return res


    def empty(self) -> bool:
        return len(self.stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()