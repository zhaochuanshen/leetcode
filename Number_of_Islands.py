'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3

Credits:
Special thanks to @mithmatt for adding this problem and creating all test cases.
'''


class Solution:
    # @param grid, a list of list of characters
    # @return an integer
    def _dfs(self,grid, i, j, visited):
        yLength = len(grid[0])
        xLength = len(grid)
        di = [1,-1,0,0]
        dj = [0,0,1,-1]
        visited[i][j] = True
        for t in xrange(4):
            if i + di[t] < 0 or i  + di[t] >= xLength or j + dj[t] < 0 or j + dj[t] >= yLength or visited[i + di[t]][j+dj[t]] or grid[i+di[t]][j+dj[t]] != '1':
                continue
            self._dfs(grid, i+di[t], j+dj[t], visited)
            
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0
        xLength = len(grid)
        yLength = len(grid[0])
        count = 0
        visited = [[False for j in xrange(yLength)]for i in xrange(xLength)]
        for i in xrange(xLength):
            for j in xrange(yLength):
                if grid[i][j] == '1' and not visited[i][j]:
                    self._dfs(grid, i, j, visited)
                    count += 1
        return count
                
            
