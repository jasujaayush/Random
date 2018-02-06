class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l = []
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        bisect.insort(self.l, num)

    def findMedian(self):
        """
        :rtype: float
        """
        n = len(self.l)
        m1 = self.l[n/2]
        m2 = self.l[(n-1)/2]
        return (m1+m2)/float(2)
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
