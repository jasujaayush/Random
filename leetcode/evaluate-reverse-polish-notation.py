class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        nums = []
        for t in tokens:
            if t == "+":
                n1 = nums[-1]
                n2 = nums[-2]
                nums = nums[:-2]
                nums.append(n2+n1)
            elif t == "-":
                n1 = nums[-1]
                n2 = nums[-2]
                nums = nums[:-2]
                nums.append(n2-n1)
            elif t == "*":
                n1 = nums[-1]
                n2 = nums[-2]
                nums = nums[:-2]
                nums.append(n2*n1)
            elif t == "/":
                n1 = nums[-1]
                n2 = nums[-2]
                nums = nums[:-2]
                result = abs(n2)/abs(n1)
                if n2<0: result *= -1
                if n1<0: result *= -1
                nums.append(result)
            else:
                nums.append(int(t))
            #print nums
        return nums[0]
                
