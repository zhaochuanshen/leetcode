'''
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
'''

class Solution:
    # @return a string
    def countAndSay(self, n):
        res = []
        res.append('1')
        for j in xrange(1, n):
            strn = res[j - 1]
            c = 1
            t = ''
            for i in xrange(1, len(strn)):
                if strn[i] == strn[i-1]:
                    c += 1
                else:
                    t = t + str(c) + strn[i-1]
                    c = 1
            res.append(t + str(c) + strn[-1])
        
        return res[n-1]
