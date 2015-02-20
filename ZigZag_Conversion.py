'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".


another example:
For PAYPALISHIRING,4, the matrix would like below, just ignore the index:

    P     I     N
    A   L S   I G
    Y A   H R
    P     I

should return "PINALSIGYAHRPI"

'''


class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows <= 1:
            return s
        table = [[] for i in xrange(nRows)]
        tableindex = 0
        upordown = 1
        for c in s:
            table[tableindex].append(c)
            tableindex += upordown
            if tableindex == nRows - 1:
                upordown = -1
            if tableindex == 0:
                upordown = 1
        
        return ''.join(map(''.join, table))
            
