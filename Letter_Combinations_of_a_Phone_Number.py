'''
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
'''

class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        d = {}
        d['2'] = ['a','b','c']
        d['3'] = ['d','e','f']
        d['4'] = ['g','h','i']
        d['5'] = ['j','k','l']
        d['6'] = ['m','n','o']
        d['7'] = ['p','q','r','s']
        d['8'] = ['t','u','v']
        d['9'] = ['w','x','y','z']
        res = ['']
        if len(digits) == 0:
            return [""]
        solutions = [""]
        for c in digits:
            if c < '2' or c > '9':
                return [""]
            solutions = [solution + i
                    for solution in solutions \
                    for i in d[c]
                ]
        return solutions
