class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_value = None

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack += [x]
        self.min_value = min(self.min_value, x)

    def pop(self):
        """
        :rtype: void
        """
        if self.min_value == self.stack[-1]:
            self.min_value = None
        self.stack.pop()
        
    
    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
    
    def checkMin(self):
        """
        :rtype: void
        """
        self.min_value = None
        
    def getMin(self):
        """
        :rtype: int
        """
        if self.min_value is None and len(self.stack) > 0:
            self.min_value = self.stack[0]
            for i in range(1, len(self.stack)):
                self.min_value = min(self.min_value, self.stack[i])
        return self.min_value


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()