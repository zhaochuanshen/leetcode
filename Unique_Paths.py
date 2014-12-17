'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
'''


class Solution:
    # @return an integer
    #@memoize
    def uniquePaths(self, m, n):
        d = {}
        return self.uniquePathhelper(m, n,d)
        
    def uniquePathhelper(self, m, n, d):
        if m == 1 or n==1:
            return 1
        try:
            return d[(m,n)]
        except:
            x = self.uniquePathhelper(m-1,n, d) + self.uniquePathhelper(m,n-1,d)
            d[(m,n)] = x
            return x
