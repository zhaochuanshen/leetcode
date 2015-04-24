'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''

class Solution:
    # @param {integer} n
    # @return {boolean}
    def squareSum(self, n):
        res = 0
        while n > 0:
            res += ( n % 10 ) * ( n % 10)
            n = n/10
        return res
        
    def isHappy(self, n):
        d = {n:True}
        while n != 1:
            x = self.squareSum(n)
            try:
                d[x]
                return False
            except:
                n = x
                d[n] = True
        return True
        
        
