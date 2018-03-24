class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        minima = None
        maxima = None
        profit = 0
        for price in prices:
            if maxima and price < maxima - fee:
                profit += (maxima - minima - fee)
                minima = price
                maxima = None
            elif (minima and price > minima + fee):
                if maxima and price> maxima:
                    maxima = price
                elif not maxima:
                    maxima = price
            elif not minima or price < minima:
                minima = price
            
            #print price, minima, maxima, profit
         
        if maxima and maxima - minima - fee > 0:
                profit += (maxima - minima - fee)
            
        return profit
        
