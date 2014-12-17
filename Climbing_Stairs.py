'''

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

'''

class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        if n <= 2:
            return n
        l = [1, 2]
        for i in xrange(2,n):
            x = l[i-1] + l[i-2]
            l.append(x)
        return l[-1]
            
        
        
