'''
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array A = [1,1,1,2,2,3],

Your function should return length = 5, and A is now [1,1,2,2,3].
'''

class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) == 0:
            return 0
        i, same = 0, 0
        for j in range(1, len(A)):
            if A[i] != A[j] or same == 0:
                same = A[i] == A[j]
                i += 1
                A[i] = A[j]
        return i + 1
            
                    
            
