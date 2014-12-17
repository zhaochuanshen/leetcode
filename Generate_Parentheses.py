'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
'''

class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        allresults = []
        for i in xrange(n+1):
            if len(allresults) == 0:
                allresults.append([''])
                continue

            newlist = [
            "(" + first +")" + second
            for j in xrange(i)
            for first in allresults[j]
            for second in allresults[i -1- j]
            ]

            allresults.append(newlist)
        return allresults[n]
