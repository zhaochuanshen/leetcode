'''
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
'''
class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        for row in board:
            d = {}
            for c in row:
                if c == '.': 
                    continue
                try:
                    d[c]
                    return False
                except:
                    d[c] = 1
        for i in xrange(len(board[0])):
            d = {}
            for j in xrange(len(board)):
                c = board[j][i]
                if c == '.':
                    continue
                try:
                    d[c]
                    return False
                except:
                    d[c] = 1
        for i in xrange(3):
            for j in xrange(3):
                d = {}
                for l in xrange(3):
                    for k in xrange(3):
                        c = board[i*3 + l][j*3 + k]
                        if c == '.':continue
                        try:
                            d[c]
                            return False
                        except:
                            d[c] = 1
        return True
        
