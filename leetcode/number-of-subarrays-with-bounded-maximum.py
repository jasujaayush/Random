class Solution(object):
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        stack = []
        count = 0
        for num in A:
            if num <= R:
                if num<L:
                    l = len(stack) - 1
                    while l>=0 and stack[l]<L:
                        l -= 1
                    count += l+1
                else:
                    count += len(stack)+1
                stack.append(num)
            else:
                stack = []
            #print num,count
        
        return count
