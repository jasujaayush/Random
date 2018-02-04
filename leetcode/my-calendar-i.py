class MyCalendar(object):

    def __init__(self):
        self.b = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for sExist,eExist in self.b:
            if start >= eExist or end <= sExist:
                continue
            else:
                return False
        self.b.append((start, end))
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
