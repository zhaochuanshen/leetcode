'''
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.
'''

class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        overall_max, running_max = -float("infinity"), 0
        for x in A:
            running_max += x
            if running_max > overall_max:
                overall_max  = running_max
            if running_max < 0:
                running_max = 0
        return overall_max
