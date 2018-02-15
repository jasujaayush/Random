class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        Awarning = False
        Lwarning = 0
        for c in s:
            if c == 'A':
                if Awarning:
                    return False
                Awarning =  True
                Lwarning = 0
            elif c== 'L':
                Lwarning += 1
                if Lwarning > 2:
                    return False
            else:
                Lwarning = 0
        return True
        
