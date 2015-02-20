'''
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.
'''


class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        left = 0
        zero = 0
        right = len(A) - 1
        while left <= right:
            if A[left] == 0:
                A[left], A[zero] = A[zero], A[left]
                left += 1
                zero += 1
            elif A[left] == 2:
                A[left], A[right] = A[right], A[left]
                right -= 1
            elif A[left] == 1:
                left += 1
