ass MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.min_stack: self.min_stack.append((x,x))
        else: self.min_stack.append((min(self.min_stack[-1][0], x), x))

    def pop(self):
        """
        :rtype: void
        """
        return self.min_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.min_stack[-1][1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1][0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
