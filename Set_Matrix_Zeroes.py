'''
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
'''

class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        def multiply(x,y): return x*y
        first_row = not reduce(multiply, matrix[0])
        first_col = not reduce(multiply, [row[0] for row in matrix])
        for i in xrange(1, len(matrix)):
            for j in xrange(1, len(matrix[0])):
                if not matrix[i][j]:
                    matrix[i][0], matrix[0][j] = 0, 0
        for i in xrange(1, len(matrix)):
            for j in xrange(1, len(matrix[0])):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0
        if first_row:
            for j in xrange(len(matrix[0])):
                matrix[0][j] = 0
        if first_col:
            for i in xrange(len(matrix)):
                matrix[i][0] = 0
