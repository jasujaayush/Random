class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        
        chars = [str(i) for i in range(10)] + ['a', 'b','c', 'd', 'e', 'f']
        hexa = ''
        
        if num<0:
            num = 2**32 - abs(num)
            
        while num:
            hexa = chars[num%16] + hexa
            num = num/16
        
        return hexa
            
        
