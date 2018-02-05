class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        duplicates = []
        for i in range(len(nums)):
            x = nums[i]
            if i == x-1:
                continue
            else:
                nums[i] = 0
                while True:
                    t = nums[x-1]
                    nums[x-1] = x
                    x = t
                    #print i,x, nums
                    if x == 0:
                        break
                    if x == nums[x-1]:
                        duplicates.append(x)
                        break
                    
        return [i+1 for i in range(len(nums)) if nums[i] == 0]
