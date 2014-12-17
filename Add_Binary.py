'''
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
'''

class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        al = list(a)
        bl = list(b)
        al = [int(i) for i in al]
        bl = [int(i) for i in bl]    
        al.reverse()
        bl.reverse()
        c = []
        jinwei = 0
        ia = 0
        ib = 0
        while ia < len(al) or ib < len(bl) or jinwei:
            if ia >= len(al):
                xa = 0
            else:
                xa = al[ia]
            if ib >= len(bl):
                xb = 0
            else:
                xb = bl[ib]
            ci = xa + xb + jinwei
            if ci > 1:
                ci -= 2
                jinwei = 1
            else:
                jinwei = 0
            c.append(ci)
            ia += 1
            ib += 1
        c = [str(i) for i in c]
        c.reverse()
        return ''.join(c)



