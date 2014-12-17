'''
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
'''

class Solution:
    # @return an integer
    def romanToInt(self, s):
        d = {}
        d['M'] = 1000
        d['D'] = 500
        d['C'] = 100
        d['L'] = 50
        d['X'] = 10
        d['V'] = 5
        d['I'] = 1
        res = 0
        i = 0
        while i < (len(s)-1):
            if d[s[i]] < d[s[i+1]]:
                res += d[s[i+1]] - d[s[i]]
                i += 2
            else:
                res += d[s[i]]
                i += 1
        if i ==  len(s) -1:
            res += d[s[-1]]
        return res
