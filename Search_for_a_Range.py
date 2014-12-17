'''
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
'''

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        s = 0
        end = len(A)-1
        #left = self.searchRangeleft(A, target, s, end)
        left = -1
        while (s <= end):
            mid = (s + end)/2
            if A[mid] < target:
                s = mid +1
            if A[mid] > target:
                end = mid - 1
            if A[mid] == target:
                if mid == 0:
                    left = 0
                    break
                if A[mid-1] != target:
                    left = mid
                    break
                else:
                    end = mid - 1
                
        if left == -1:
            return [-1, -1]
        right = -1
        s, end = 0, len(A)-1
        while (s <= end):
            mid = (s + end)/2
            if A[mid] > target:
                end = mid - 1
            if A[mid] < target:
                s = mid + 1
            if A[mid] == target:
                if mid == len(A)-1:
                    right = mid
                    break
                if A[mid + 1] != target:
                    right = mid
                    break
                else:
                    s = mid + 1
        return [left, right]
