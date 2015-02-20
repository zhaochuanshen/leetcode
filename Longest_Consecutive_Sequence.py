'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
'''


class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        d = {}
        longest = 0
        for inte in num:
            try:
                d[inte]
            except:
                try:
                    left = d[inte-1]
                except:
                    left = 0
                try:
                    right = d[inte+1]
                except:
                    right = 0
                distance = left +right + 1
                d[inte - left] = distance
                d[inte + right] = distance
                d[inte] = distance
                longest = max(distance, longest)
        return longest
