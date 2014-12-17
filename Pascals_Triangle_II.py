'''
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
'''


def memoize(function):
    memo = {}
    def wrapper(*args):
        if args in memo:
            return memo[args]
        else:
            rv = function(*args)
            memo[args] = rv
        return rv
    return wrapper

class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        
        @memoize
        def _getRow(rowIndex):
            if rowIndex == 0:
                return [1]
            if rowIndex == 1:
                return [1,1]
            if rowIndex == 2:
                return [1,2,1]
            l = _getRow(rowIndex - 1)
            res = []
            for i in xrange(len(l)-1):
                res.append(l[i] + l[i+1])
            res.insert(0,1)
            res.append(1)
            return res
        
        
        
        return _getRow(rowIndex)

