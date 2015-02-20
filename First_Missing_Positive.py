'''
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
'''

class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        for i in xrange(len(A)):
            num = A[i]
            while num > 0 and num < len(A) and A[num -1 ]!=num:
                A[i], A[num-1] = A[num-1], A[i]
                num = A[i]
                
        for i, elem in enumerate(A):
            if elem != i+1:
                return i + 1
        
        return len(A)+1
        
