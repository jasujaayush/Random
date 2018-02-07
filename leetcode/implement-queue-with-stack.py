class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.inbox = []
        self.outbox = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.inbox.append(x) #push in stack
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self.outbox) == 0:
            while len(self.inbox):
                self.outbox.append(self.inbox.pop())
        return self.outbox.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self.outbox) == 0:
            while len(self.inbox):
                self.outbox.append(self.inbox.pop())
        return self.outbox[-1]
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.outbox) + len(self.inbox)  == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
