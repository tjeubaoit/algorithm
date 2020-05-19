class MyQueue:
    """
    Push O(1), pop best at O(1), worst at O(n)
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.first = []
        self.second = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.first.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.ensure_second_not_empty()
        return self.second.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        self.ensure_second_not_empty()
        return self.second[-1] if self.second else None

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.first) == 0 and len(self.second) == 0

    def ensure_second_not_empty(self):
        if not self.second:
            while self.first:
                self.second.append(self.first.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
