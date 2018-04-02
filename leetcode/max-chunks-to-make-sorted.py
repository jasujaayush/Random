class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count = 0
        nex = arr[0]
        i = 0
        while i<=len(arr):
            if i == len(arr) and nex == len(arr)-1:
                count += 1
            elif i > nex:
                count += 1
                nex = arr[i]
            else:
                nex = max(nex,arr[i])
            
            i += 1
        
        return count
        
