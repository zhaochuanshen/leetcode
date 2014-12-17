
'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.
'''

class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        m = len(matrix)-1
        n = len(matrix[0])-1
        if target < matrix[0][0] or target > matrix[m][n]:
            return False
        s, end = 0, m
        row = -1
        while s <= end:
            mid = (s+end)/2
            if target < matrix[mid][0]:
                end = mid - 1
            if target > matrix[mid][n]:
                s = mid +1
            if target <= matrix[mid][n] and target >= matrix[mid][0]:
                row = mid
                break
        if row == -1:
            return False
        s, end = 0, n
        while s <= end:
            mid = (s+end)/2
            if target == matrix[row][mid]:
                return True
            if target < matrix[row][mid]:
                end = mid - 1
            if target > matrix[row][mid]:
                s = mid + 1
        return False
            
