'''
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

For example, given the range [5, 7], you should return 4.
'''


class Solution:
    # @param m, an integer
    # @param n, an integer
    # @return an integer
    def rangeBitwiseAnd(self, m, n):
        if m == n:
            return m
        diff = int( math.log(n-m,2) ) +1
        m = m >> diff
        n = n >> diff
        return (m&n) << diff
