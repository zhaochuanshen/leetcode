'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1].
'''

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        d = {}
        for i in num:
            try:d[i] += 1
            except:d[i] = 1

        solutions = [[]]
        num1 = set(num)
        for item in xrange(len(num)):
            solutions =  [solution + [i] \
                for solution in solutions \
                for i in num1 \
                if solution.count(i) < d[i]  ]
        
        return list(solutions)
