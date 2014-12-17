'''
Given an array of integers, every element appears three times except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
'''

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        d = {}
        for i in A:
            try:
                d[i] += 1
            except:
                d[i] = 1
        for i in d.keys():
            if d[i] ==1 :
                return i

