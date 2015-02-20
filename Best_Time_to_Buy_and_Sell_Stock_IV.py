'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
'''


class Solution:
    # @return an integer as the maximum profit 
    def maxProfit(self, k, prices):
        if len(prices) < 2:
            return 0
        
        if k > len(prices) / 2:
            profit = 0
            for i in xrange(1, len(prices)):
                if prices[i] > prices[i-1]:
                    profit += prices[i] - prices[i-1]
            return profit
                
        f = [[0 for j in xrange( len(prices) ) ] for i in xrange(k + 1)]
        for kk in xrange(1, k+1 ):
            temp = f[kk-1][0] - prices[0]
            for i in xrange(1, len(prices)):
                temp = max(f[kk-1][i-1] - prices[i-1], temp)
                f[kk][i] = max(f[kk][i-1], prices[i] + temp)
                
        return f[k][-1]
