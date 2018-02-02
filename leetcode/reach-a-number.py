class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        #pattern of bfs = [-sum, -sum+2, ----, sum]
        count = 0
        k = 0
        while True:
            k = k + count
            if k>= abs(target) and k%2 == target%2:
                return count
            count += 1
