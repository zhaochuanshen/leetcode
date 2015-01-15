'''
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''


class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        # I find this solution online
        results = []
        def _combine(current, n, k, i):
            if k == 0:
                return [current]
            if i > n:
                return []
            return _combine(current, n, k, i+1) + _combine(current + [i], n, k-1, i+1)
        return _combine(results, n, k, 1)
