'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
'''

class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        answer = [[0 for j in xrange(len(grid[0]))] for i in xrange(len(grid))]
        answer[0][0] = grid[0][0]
        for i in xrange(1, len(grid)):
            answer[i][0] = answer[i-1][0] + grid[i][0]
        for j in xrange(1, len(grid[0])):
            answer[0][j] = answer[0][j-1] + grid[0][j]
        for i in xrange(1, len(grid)):
            for j in xrange(1, len(grid[0])):
                answer[i][j] = min(answer[i-1][j], answer[i][j-1]) + grid[i][j]
                
        return answer[-1][-1]
