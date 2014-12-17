'''
Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.
'''


class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def search(self, A, target):
        s = 0
        end = len(A) - 1
        return self.searchHelper(A, target, s, end)
    
    def searchHelper(self, A, target, s, end):
        if s > end:
            return False
        mid = (s + end)/2
        if A[mid] == target: return True
        if A[mid] > A[s]: # left is sorted
            if target < A[mid] and target >= A[s]:
                return self.searchHelper(A, target, s, mid-1)
            else:
                return self.searchHelper(A, target, mid+1, end)
        if A[mid] < A[end]: # right is sorted
            if target > A[mid] and target <= A[end]:
                return self.searchHelper(A, target, mid+1, end)
            else:
                return self.searchHelper(A, target, s, mid-1)
        if A[s] == target:
            return True
        return self.searchHelper(A, target, s+1, end)
        
