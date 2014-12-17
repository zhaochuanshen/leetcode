'''
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
'''

class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        digits.reverse()
        digits[0] += 1
        for i in xrange(len(digits)):
            if digits[i] <= 9:
                break
            else:
                if i < len(digits)-1:
                    digits[i] -= 10
                    digits[i+1] += 1
        
        if digits[-1] > 9:
            digits[-1] -= 10
            digits.append(1)
        digits.reverse()
        return digits
        
