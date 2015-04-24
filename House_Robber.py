'''

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

'''


class Solution:
    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
        if len(num) == 0:
            return 0
        result = [0 for i in xrange( len(num) )]
        for i in xrange( len(num) ):
            if i == 0:
                result[i] = num[i]
            if i == 1:
                result[i] = max(num[1],num[0])
            if i > 1:
                result[i] = max(result[i-2] + num[i], result[i-1])
        return result[-1]
