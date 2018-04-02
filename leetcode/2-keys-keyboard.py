class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        clip = board = 1
        rem = n-clip
        ops = 0
        while rem>0:
            #print board, clip, rem
            if rem%board == 0: #copy
                clip = board
                ops += 1
                
            #paste
            rem -= clip
            board += clip
            ops += 1
        
        return ops
                
