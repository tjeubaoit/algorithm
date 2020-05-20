from queue import SimpleQueue
from collections import deque


class MyStack1:
    """
    Push O(1), pop O(n)
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = SimpleQueue()
        self.q2 = SimpleQueue()
        self.front = None

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q1.put(x)
        self.front = x

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.q2.empty():
            while self.q1.qsize() > 1:
                self.front = self.q1.get()
                self.q2.put(self.front)
            self.q1, self.q2 = self.q2, self.q1
        return self.q2.get()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.front

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.q1.empty()


class MyStack2:
    """
    Push O(n), pop O(1)
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
stack = MyStack1()
stack.push(1)
stack.push(2)
print(stack.top())
print(stack.pop())
print(stack.empty())
