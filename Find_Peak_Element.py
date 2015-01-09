'''
A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.

Note:
Your solution should be in logarithmic complexity.
'''

class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        low = 0
        high = len(num) - 1
        while low < high:
            if low + 1 == high:
                if num[low] < num[high] :
                    return high
                else:
                    return low
            mid = (low + high) /2
            if num[mid - 1] < num[mid]  and num[mid + 1] < num[mid]:
                return mid
            if num[mid - 1] < num[mid] and num[mid + 1] > num[mid]:
                low= mid + 1
            if num[mid - 1] > num[mid] and num[mid + 1] < num[mid]:
                high  = mid -1
            if num[mid - 1] > num[mid] and num[mid + 1] > num[mid]:
                high = mid - 1
        return low
        
