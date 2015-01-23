'''
Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.
'''



class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        def _compare(a, b):
            if a + b < b + a:
                return 1
            if a + b == b + a:
                return 0
            return -1
        s = map(str, num)
        s.sort(cmp = _compare)
        return str( int("".join(s)) )
