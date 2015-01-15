'''
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array A = [1,1,2],

Your function should return length = 2, and A is now [1,2].
'''



class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) == 0:
            return len(A)
        i = 0
        j = 1
        curr = A[0]
        while j < len(A):
            if curr != A[j]:
                curr = A[j]
                i += 1
                A[i] = curr
            j += 1
        return i+1
