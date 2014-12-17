'''
Given two numbers represented as strings, return multiplication of the numbers as a string.

Note: The numbers can be arbitrarily large and are non-negative.
'''

class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        n1list = list(num1) 
        n2list = list(num2)
        total = [0 for i in xrange(len(num1) + len(num2))]
        i = 0
        for n1 in reversed(n1list):
            j = 0
            for n2 in reversed(n2list):
                temp = int(n1) *int(n2)
                total[i+j] += temp - (temp / 10 ) *10
                k = i +j
                while  total[k] >= 10:
                    total[k] -= 10
                    total[k + 1] += 1
                    k += 1
                total[i+j+1] += temp /10
                k = i + j + 1
                while total[k] >= 10:
                    total[k] -= 10
                    total[k + 1] += 1
                    k += 1
                j += 1
            i += 1
        totalstring = [str(i) for i in reversed(total)]
        for i in xrange(len(totalstring)):
            if totalstring[i] != '0':
                break
            
        return "".join(totalstring[i:])

