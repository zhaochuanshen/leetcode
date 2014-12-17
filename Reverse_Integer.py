'''
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321
'''

class Solution:
    # @return an integer
    def reverse(self, x):
        if x == 0:
            return x
            
        if x > 0:
            res = 0
            y = x
            lastdigit = 0
            while (y > 0):
                lastdigit = y % 10
                res = res * 10 +lastdigit
                y = y /10
            return res
        if x < 0:
            return -self.reverse(-x)
        
