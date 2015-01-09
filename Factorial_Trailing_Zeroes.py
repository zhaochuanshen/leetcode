'''
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.
'''

import math

class Solution:
    # @return an integer
	def trailingZeroes(self, n):
		if n == 0: return 0
		upper = int(math.log(n, 5))
		result = 0
		for i in xrange(1, upper + 1):
			result = result + n / (5**i)        
		return result
