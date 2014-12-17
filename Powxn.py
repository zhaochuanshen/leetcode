'''

Implement pow(x, n).
'''

class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if n < 0:
            return 1./self.pow(x, -n)
        
        res = 1
        k = n
        while k > 0:
            if k%2 :
                res *= x
            x *= x
            k /= 2
        return res
        


