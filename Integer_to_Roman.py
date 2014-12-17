'''
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
'''

class Solution:
    # @return a string
    def intToRoman(self, num):
        if num == 0:
            return ''
        if num -1000 >= 0:
            return 'M' + self.intToRoman(num - 1000)
        if num >= 900:
            return 'CM' + self.intToRoman(num - 900)
        if num >= 500:
            return 'D' +  self.intToRoman(num - 500)
        if num >= 400:
            return 'CD' +  self.intToRoman(num - 400)    
        if num >= 100:
            return 'C' + self.intToRoman(num - 100)
        if num >= 90:
            return 'XC' + self.intToRoman(num - 90)
        if num >= 50:
            return 'L' + self.intToRoman(num - 50)
        if num >= 40:
            return 'XL' + self.intToRoman(num - 40)
        if num >= 10:
            return 'X' + self.intToRoman(num - 10)
        if num >= 9:
            return 'IX' + self.intToRoman(num - 9)
        if num >= 5:
            return 'V' + self.intToRoman(num - 5)
        if num == 4:
            return 'IV'
        return num * 'I'
