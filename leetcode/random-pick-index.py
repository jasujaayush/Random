class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums
        #from collections import defaultdict
        #self.indexMap = defaultdict(list)
        #for i in range(len(nums)):
        #    self.indexMap[nums[i]] += [i]
        

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        indices = [i for i in range(len(self.nums)) if self.nums[i] == target]
        result = 0
        length = len(indices)#self.indexMap[target]
        index = 1
        while index < length:
            r = random.randint(0,index)
            if r == 0: #If random lies within the window of reservoir (0 in this case), replace it with new value
                result = index
            index += 1
        return indices[result]#self.indexMap[target][result]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
