class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def generate(i, results):
            if i <= n:
                results.append(i)
                if i*10 <= n:
                    for x in range(10):
                        y = i*10 + x
                        generate(y,results)
                        
        results = []
        for i in range(1,10):
            generate(i,results)
        
        return results
        
        
        
        
