class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0:
            return []
        
        summary = []
        start = nums[0]
        count = 1
        for n in nums[1:]:
            if n == start + count: 
                count += 1
            else:
                if count == 1:
                    summary.append(str(start))
                else:
                    summary.append(str(start) + "->" + str(start+count-1))
                start = n
                count = 1
        
        if count == 1:
            summary.append(str(start))
        else:
            summary.append(str(start) + "->" + str(start+count-1))
                
            
        return summary
            
            
        
