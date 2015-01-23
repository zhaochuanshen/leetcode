'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
'''

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
        minprice = prices[0]
        result = 0
        for pr in prices:
            if pr < minprice:
                minprice = pr
            if pr- minprice > result:
                result = pr - minprice
        return result
