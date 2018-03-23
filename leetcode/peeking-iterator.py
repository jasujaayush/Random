# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator(object):
    def __init__(self, it):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.it = it
        self.top = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.top == None:
            self.top = self.it.next()
        return self.top
        

    def next(self):
        """
        :rtype: int
        """
        if self.top != None:
            r = self.top
            self.top = None
            return r
        
        return self.it.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.top != None:
            return True
        return self.it.hasNext()

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
