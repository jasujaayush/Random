class Solution(object):
    def getMoneyAmount(self, n):
        money = [[0]*(n+1) for i in range(n+1)]
        for low in range(n,0,-1):
            for high in range(low+1, n+1):
                money[low][high] = min(x + max(money[low][x-1], money[x+1][high]) for x in range(low, high))
        return money[1][n]

                  
