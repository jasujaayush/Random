class Solution(object):
    def getStr(self, i):
        if (i%15 == 0):
            return "FizzBuzz" 
        elif i%5==0:
            return "Buzz" 
        elif i%3==0:
            return "Fizz"
        else:
            return str(i)
    
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return [self.getStr(i) for i in range(1,n+1)]
