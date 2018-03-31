class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        ones = 0
        zeros = 0
        prev = None
        for i, c in enumerate(s):
            if prev and c!= prev:
                total += min(zeros, ones)
                ones = ones*int(c=='0')
                zeros = zeros*int(c=='1')
            
            ones += int(c == '1')
            zeros += int(c == '0')
            prev = c
        
        total += min(zeros, ones)
        return total
                
            
        
            
