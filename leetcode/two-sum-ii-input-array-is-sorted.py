class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i in range(len(numbers)):
            n = numbers[i]
            
            if d.has_key(target-n):
                return [d[target-n]+1, i+1]
            elif not d.has_key(n):
                d[n] = i
            
