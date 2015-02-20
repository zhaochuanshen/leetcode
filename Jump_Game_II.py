'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
'''


class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        if len(A) < 2:
            return 0
        level = 0
        i = 0
        currentmax = 0
        overallmax = 0
        while i < len(A):
            level += 1
            for j in xrange(i, min(currentmax + 1, len(A)) ):
                overallmax = max(overallmax, j + A[j])
            if overallmax >= len(A) - 1:
                return level
            if overallmax == i:
                return -1
            i = currentmax 
            currentmax = overallmax
        
            
