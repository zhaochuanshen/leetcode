'''
Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of distinct solutions.
'''

class Solution:
    # @return an integer
    def under_attack(self, i, existing_queens):
        return i in existing_queens or any( abs(i - x) == len(existing_queens)-j   for j,x in enumerate(existing_queens)    )
    
    def totalNQueens(self, n):
        if n == 1:
            return 1
        solutions = [[]]
        for item in xrange(n):
            solutions = [solution + [i] \
                            for solution in solutions \
                            for i in xrange(n)
                            if not self.under_attack(i, solution)
                ]
        #if not solutions[0]:
        #    return 0
        #else: 
        return len(solutions)

