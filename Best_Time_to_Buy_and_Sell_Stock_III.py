'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).


'''
'''
this beautiful algorithm is due to @peterleetcode
// f[k, ii] represents the max profit up until prices[ii] (Note: NOT ending with prices[ii]) using at most k transactions. 
        // f[k, ii] = max(f[k, ii-1], prices[ii] - prices[jj] + f[k-1, jj]) { jj in range of [0, ii-1] }
        //          = max(f[k, ii-1], prices[ii] + max(f[k-1, jj] - prices[jj]))
        // f[0, ii] = 0; 0 times transation makes 0 profit
        // f[k, 0] = 0; if there is only one price data point you can't make any money no matter how many times you can trade
'''

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        k = 2
        if len(prices) < 2:
            return 0
        f = [[0 for j in xrange( len(prices) ) ] for i in xrange(k + 1)]
        for kk in xrange(1, k+1 ):
            temp = f[kk-1][0] - prices[0]
            for i in xrange(1, len(prices)):
                temp = max(f[kk-1][i-1] - prices[i-1], temp)
                f[kk][i] = max(f[kk][i-1], prices[i] + temp)
                
        return f[k][-1]
