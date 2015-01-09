'''
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".
'''

class Solution:
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        if numerator == 0:
            return '0'
        res = ''
        if numerator * denominator < 0:
            res += '-' # take care of the sign
        denominator = abs(denominator)
        numerator = abs (numerator)
        res += str(numerator / denominator)
        if numerator == numerator / denominator * denominator:
            return res
        remain = numerator - numerator / denominator * denominator
        res += '.'
        i = 0
        remain *= 10
        d = {}
        afterd = []
        while True: # this is a simulation of the calculation of division
            try:
                left = d[remain] 
				# this is a repeated remainder, indicating that we can end the braket
                afterd.insert(left, '(')
                afterd.append(')')
                break
            except:
                d[remain] = i
                shang = remain / denominator
                afterd.append(str(shang) )
                remain = remain - shang * denominator
                if remain == 0:
                    break # without this if, we could have something like 0.5(0)
                remain *= 10
                i += 1
        return res + ''.join(afterd)
