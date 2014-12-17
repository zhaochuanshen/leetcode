'''
Given an array and a value, remove all instances of that value in place and return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
'''

class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        count = 0
        for i in xrange(len(A)):
            if A[i] == elem:
                count += 1
            else:
                if count > 0:
                    A[i - count] = A[i]
                
        return len(A) - count
        
