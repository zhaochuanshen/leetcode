'''
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''

def memoize(function):
    memo = {}
    def wrapper(*args):
        try:
            return memo[args]
        except:
            rv = function(*args)
            memo[args] = rv
        return rv
    return wrapper

class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        
        @memoize
        def _generate(numRows):
            if numRows == 0:
                return []
            if numRows == 1:
                return [[1]]
            if numRows == 2:
                return [[1],[1,1]]
            l1 = _generate(numRows - 1)[-1]
            newl = []
            for i in xrange(len(l1)-1):
                newl.append(l1[i] + l1[i+1])
            newl.insert(0,1)
            newl.append(1)
                
            return _generate(numRows - 1) + [newl]
        
        
        return _generate(numRows)
        
