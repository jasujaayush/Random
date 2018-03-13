class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        index = [0]*len(primes)
        result = [1]
        
        for i in range(n):
            result.append( min([p*result[index[i]]   for i,p in enumerate(primes)]))
            for i,p in enumerate(primes):
                if p*result[index[i]] == result[-1]:
                    index[i] += 1
        return result[n-1]
