class Solution(object):
    def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        mem = {}
        def best(n,k):
            if (n,k) in mem:
                return mem[(n,k)]
            
            if k == 1:
                mem[(n,k)] = sum(A[:n])/float(n)
                return mem[(n,k)]
            
            mem[(n,k)] = 0
            sofar = 0
            for i in range(n-1,0,-1):
                sofar += A[i]
                mem[(n,k)] = max(mem[(n,k)], sofar/float(n-i)+best(i,k-1))
            return mem[(n,k)]
        
        return best(len(A),K)
            
