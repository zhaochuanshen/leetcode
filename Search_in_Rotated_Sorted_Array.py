'''
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
'''

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        s = 0
        end = len(A) - 1
        return self.searchHelper(A, target, s, end)
    
    def searchHelper(self, A, target, s, end):
        if s == end:
            if A[s] == target:
                return s
            else:
                return -1
        mid = (s + end)/2
        if ( A[mid] > A[s] and (target < A[s] or target > A[mid]) ) or (A[mid] <= A[s] and (target >= A[mid+1] and target <= A[end]) ):
            return self.searchHelper(A, target, mid +1, end)
        else:
            return self.searchHelper(A, target, s, mid)
