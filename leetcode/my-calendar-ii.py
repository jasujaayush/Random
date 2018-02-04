class MyCalendarTwo(object):

    def __init__(self):
        self.b = []
        self.db = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for os,oe in self.db:
            if start >= oe or end <= os:
                continue
            else:
                return False
        
        for sExist,eExist in self.b:
            if start >= eExist or end <= sExist:
                continue
            else:
                self.db.append((max(sExist, start), min(eExist, end)))
                
        self.b.append((start, end))
        return True
    

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
