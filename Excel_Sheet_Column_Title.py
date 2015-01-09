'''
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
'''


class Solution:
    # @return a string
    def convertToTitle(self, num):
        result = []
        while num > 0:
            x = num % 26
            if x == 0: 
                x =  26
            result.insert(0, chr(x + ord('A') - 1) )
            num = (num - x)/26
        return ''.join(result)
