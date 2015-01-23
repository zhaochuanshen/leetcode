'''
Best Time to Buy and Sell Stock II Total Accepted: 35166 Total Submissions: 94505 My Submissions Question Solution 
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
'''

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        result = 0
        inhand = False
        for i in xrange(len(prices) -1):
            if prices[i] <= prices[i+1]:
                if not inhand:
                    buy = prices[i]
                    inhand = True
            else:
                if inhand:
                    result += prices[i] - buy
                    inhand = False
        if inhand:
            result += prices[-1] - buy
        return result
