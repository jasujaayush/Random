class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        if len(bits) == 0:
            return False
        
        if len(bits) == 1 and bits[0] == 0:
            return True
        
        if bits[0] == 0:
            return self.isOneBitCharacter(bits[1:])
        elif bits[0] == 1:
            return self.isOneBitCharacter(bits[2:])
        
        return False
