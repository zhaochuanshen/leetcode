'''
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.
'''


class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer

    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        res = [[0 for j in xrange(n)]for i in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                if obstacleGrid[i][j] == 0:
                    if i == 0 and j == 0:
                        res[i][j] = 1
                    if i == 0 and j != 0:
                        res[i][j] = res[i][j-1]
                    if i != 0 and j ==0:
                        res[i][j] = res[i-1][j]
                    if i > 0 and j>0:
                        res[i][j] = res[i-1][j] + res[i][j-1]
        return res[-1][-1]
