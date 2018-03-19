class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if not num:
            return "0"
        
        sign = (num < 0)
        num = abs(num)
        result = ""
        i = 0
        while num:
            result  = str(num%7) + result
            num = num/7
            i+=1
        return "-" + result if sign else result
