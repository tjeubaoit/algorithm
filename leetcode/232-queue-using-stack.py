class MyQueue:
    """
    Push O(1), pop best at O(1), worst at O(n)
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.s1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.ensure_second_not_empty()
        return self.s2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        self.ensure_second_not_empty()
        return self.s2[-1] if self.s2 else None

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.s1) == 0 and len(self.s2) == 0

    def ensure_second_not_empty(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
