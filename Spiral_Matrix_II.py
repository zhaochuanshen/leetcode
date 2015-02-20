'''
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

'''

lass Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        result = [[0 for i in xrange(n)] for j in xrange(n)]
        col_s,row_s = 0, 0
        col_e, row_e = n,n
        x = 1
        while x <= n*n:
            for i in xrange(col_s, col_e):
                result[row_s][i] = x
                x += 1
            row_s += 1
            if row_s >= row_e: break
            for j in xrange(row_s, row_e):
                result[j][col_e-1] = x
                x += 1
            col_e -= 1
            if col_s >= col_e: break
            for i in reversed(xrange(col_s, col_e)):
                result[row_e-1][i] = x
                x += 1
            row_e -= 1
            if row_s >= row_e: break
            for j in reversed(xrange(row_s, row_e)):
                result[j][col_s] = x
                x += 1
            col_s += 1
            if col_s >= col_e: break
        return result
