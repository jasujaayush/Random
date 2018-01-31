class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        string = '1'
        for i in range(1,n):
            newString = ''
            count = 0
            prev = ''
            for current in string:
                if prev=='' or current==prev:
                    prev = current
                    count+=1
                else:
                    newString += str(count) + prev
                    prev = current
                    count = 1
            if count>0:
                newString += str(count) + prev
            string = newString
        return string
