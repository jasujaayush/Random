class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        
        self.s = []
        t = 0
        for num in nums:
            t += num
            self.s.append(t)
        
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.s[j] - (self.s[i-1] if i>0 else 0)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
