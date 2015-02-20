'''
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Do it in-space
'''



class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        matrix.reverse()
        for i in xrange(len(matrix) ):
            for j in xrange( len(matrix) ):
                if i <= j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix
