'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.


'''


class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        count = 0
        # this so-called Moore voting algorithm
        for i in xrange(len(num)):
            if count == 0:
                candidate = num[i]
                count += 1
            else:
                if num[i] == candidate:
                    count += 1
                else:
                    count -= 1
        return candidate    
