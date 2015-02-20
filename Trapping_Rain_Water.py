'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
'''



class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        left = 0
        right = len(A) - 1
        leftmax, rightmax = 0,0
        res = 0
        while left < right:
            if A[left] < A[right]:
                if A[left] >= leftmax:
                    leftmax = A[left]
                else:
                    res += leftmax - A[left]
                left += 1
            else:
                if A[right] >= rightmax:
                    rightmax = A[right]
                else:
                    res += rightmax - A[right]
                right -= 1
        return res
