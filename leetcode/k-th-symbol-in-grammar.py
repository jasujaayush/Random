class Solution(object):
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        if K==1:
            return 0
        
        #print N,K
        if K > 2**(N-2):
            K = K - 2**(N-2)
            return 1 - self.kthGrammar(N-1, K)
        else:
            return self.kthGrammar(N-1, K)
