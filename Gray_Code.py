'''
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2
Note:
For a given n, a gray code sequence is not uniquely defined.
'''


class Solution:
    # @return a list of integers
    def grayCode(self, n):
        res = [0]
        for i in xrange(0, n):
            res += [x + pow(2, i) for x in reversed(res)]
        return res
