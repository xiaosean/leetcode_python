class MyStack:

    def __init__(self):
        self.queue = []
        self.temp = []

    def push(self, x: int) -> None:
        self.queue += [x]

    def pop(self) -> int:
        self.temp = []
        last_element = None
        while self.queue:
            if last_element:
                self.temp += [last_element]    
            last_element = self.queue[0] 
            del self.queue[0] 
        self.queue = self.temp
        return last_element

    def top(self) -> int:
        self.temp = []
        last_element = None
        while self.queue:
            self.temp += [self.queue[0]]    
            last_element = self.queue[0] 
            del self.queue[0]
        self.queue = self.temp
        return last_element

    def empty(self) -> bool:
        return len(self.queue) == 0        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()