class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stacks = []
        self.temp = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stacks += [x]

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        res = None
        while self.stacks:
            res = self.stacks[-1]
            self.temp += [self.stacks[-1]]
            del self.stacks[-1]
        if self.temp:
            del self.temp[-1]
        while len(self.temp):
            self.stacks += [self.temp[-1]]
            del self.temp[-1]
        return res

    def peek(self) -> int:
        """
        Get the front element.
        """
        while self.stacks:
            res = self.stacks[-1]
            self.temp += [self.stacks[-1]]
            del self.stacks[-1]
        while len(self.temp):
            self.stacks += [self.temp[-1]]
            del self.temp[-1]
        return res

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stacks) == 0
            


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()