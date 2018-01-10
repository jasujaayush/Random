class Solution(object):
    def canPlaceFlowers(self, flowerbed, nums):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        l = [0] + flowerbed + [0]
        for i in range(1, len(l)-1):
            if l[i] == 0 and l[i-1] == 0 and l[i+1] == 0:
                l[i] = 1
                nums -= 1
        
        return nums <= 0
