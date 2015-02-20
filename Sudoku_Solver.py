class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):	
		def _isValid(workingboard, row, col):
			c = workingboard[row][col]
			for c1 in xrange(0,9):
				if c1 != col and workingboard[row][c1] == c:
					return False
			for r1 in xrange(0,9):
				if r1 != row and workingboard[r1][col] == c:
					return False
			rrange = xrange((row / 3)*3, (row /3)*3 +3)
			crange = xrange((col/3)*3, (col/3)*3 + 3)
			for r1 in rrange:
				for c1 in crange:
					if r1 != row and c1 != col and workingboard[r1][c1] == c:
						return False
			return True
			
		def _solveSudoku(index):
			if index == 81:
				return True
			row, col = divmod(index, 9)
			if workingboard[row][col] != '.':
				return _solveSudoku(index + 1)
			for i in xrange(1, 10):
				workingboard[row][col] = str(i)
				x = _isValid(workingboard, row, col)
				if x:
					y = _solveSudoku(index + 1)
					if y:
						return True
			workingboard[row][col] = '.'
			return False
		workingboard = [list(li) for li in board]
		_solveSudoku(0)
		for i in xrange(0,9):
			board[i] = ''.join(workingboard[i])
