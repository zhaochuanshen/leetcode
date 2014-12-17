'''
Determine whether an integer is a palindrome. Do this without extra space.
'''

class Solution:
    # @return a boolean
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
    def isPalindrome(self, x):
        if x<0:
            return False
        y = self.reverse(x)
        if x == y:
            return True
        else:
            return False
        
