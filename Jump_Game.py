'''

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
'''



class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        reach = 0
        if len(A) == 1:
            return True
        for i, Ai in enumerate(A):
            if i > reach:
                return False
            reach = max(i+Ai, reach)
            if reach >= len(A):
                return True
        return len(A) -1 <= reach
