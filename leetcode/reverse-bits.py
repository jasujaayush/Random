class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        r = 0
        for i in range(32):
            if n&(2**i):
                r += 2**(31-i)   
        return r
