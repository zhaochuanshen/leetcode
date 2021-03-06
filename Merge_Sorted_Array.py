'''
Given two sorted integer arrays A and B, merge B into A as one sorted array.

Note:
You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B. The number of elements initialized in A and B are m and n respectively.
'''

class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        last = m + n -1
        i = m - 1
        j = n - 1
        while i >=0 and j >= 0:
            if A[i] >= B[j]:
                A[last] = A[i]
                i = i-1
            else:
                A[last] = B[j]
                j = j -1
            last = last -1
        
        if i < 0:
            A[:last+1] = B[:j+1]
