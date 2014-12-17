'''
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
'''

class Solution:
    # @return a list of lists of string
    def under_attack(self,col, queens):
        return col in queens or \
           any(abs(col - x) == len(queens)-i for i,x in enumerate(queens))
 
    def solve(self,n):
        solutions = [[]]
        for row in range(n):
            solutions = [solution+[i]
                       for solution in solutions
                       for i in range(n)
                       if not self.under_attack(i, solution)]
        return solutions
        
    def solveNQueens(self, n):
        if n == 1:
            return [["Q"]]

        if n <4:
            return []
        result = self.solve(n)
        printout = []
        for vec in result:
            candi = []
            for i in vec:
                candi.append("".join(['.'*i,'Q','.'*(n-1-i)])    )
            printout.append(candi)
        return printout
