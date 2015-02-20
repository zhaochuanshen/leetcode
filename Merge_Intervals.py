'''
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
'''
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        def _compare_intervals(a, b):
            if a.start <  b.start:
                return -1
            elif a.start > b.start:
                return 1
            return 0
        intervals.sort(cmp = _compare_intervals)
        if len(intervals) == 0:
            return []
        result = [intervals[0]]
        for inte in intervals:
            if inte.start > result[-1].end:
                result.append(inte)
            else:
                result[-1].end = max(result[-1].end,inte.end)
        return result
            
        
