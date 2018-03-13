class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        primes = [2,3,5]
        index = [0]*len(primes)
        result = [1]
        
        for i in range(n):
            result.append( min([p*result[index[i]]   for i,p in enumerate(primes)]))
            for i,p in enumerate(primes):
                if p*result[index[i]] == result[-1]:
                    index[i] += 1
        return result[n-1]
