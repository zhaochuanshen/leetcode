'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
'''


class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        result = []
        if not matrix:
            return result
        row_s = 0
        row_e = len(matrix)
        col_s = 0
        col_e = len(matrix[0]) 
        size = row_e * col_e
        while len(result) < size:
            for i in xrange(col_s, col_e):
                result.append(matrix[row_s][i])
            row_s += 1
            if row_s >= row_e: break
            for j in xrange(row_s, row_e):
                result.append(matrix[j][col_e-1])
            col_e -= 1
            if col_s >= col_e: break
            for i in reversed(xrange(col_s, col_e)):
                result.append(matrix[row_e-1][i])
            row_e -= 1
            if row_s >= row_e: break
            for j in reversed(xrange(row_s, row_e)):
                result.append(matrix[j][col_s])
            col_s += 1
            if col_s >= col_e: break
        return result
