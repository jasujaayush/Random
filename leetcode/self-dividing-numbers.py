class Solution(object):
    def giveNumbersOfLength(self, length):
        start = 10**(length-1)
        end = 10**(length)
        return range(start, end)
    
    def selfDivisible(self, number):
        strn = str(number)
        for n in strn:
            n = int(n)
            if (n == 0) or (number%n != 0):
                return False
        return True
    
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        length_left = len(str(left))
        length_right = len(str(right))
        answer = []
        for length in range(length_left, length_right+1):
            numbers = self.giveNumbersOfLength(length)
            for number in numbers: 
                if number >= left and number <= right and self.selfDivisible(number):
                    answer.append(number)
        return answer
                        
        
