'''
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Try to solve it in linear time/space.

Return 0 if the array contains less than 2 elements.

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
'''


import math

class Solution:
    # @param num, a list of integer
    # @return an integer
    def maximumGap(self, num):
        length = len(num)
        if length < 2:
            return 0
        if length == 2:
            return abs(num[0] - num[1])
        minn = min(num)
        maxx = max(num)
        maxarray = [-float('infinity') for _ in xrange(len(num)-1)]
        minarray = [float('infinity') for _ in xrange(len(num)-1)]
        
        step = int( math.ceil( (maxx - minn) / float(length - 1) ) )
        
        for inte in num:
            if inte == minn or inte == maxx:
                continue
            index = (inte - minn) / step
            if maxarray[index] < inte:
                maxarray[index] = inte
            if minarray[index] > inte:
                minarray[index] = inte
        
        maxgap = -float('infinity')
        prev = minn
        for i in xrange(len(minarray)):
            if minarray[i] == float('infinity') or maxarray[i] == -float('infinity'):
                continue
            maxgap = max(maxgap, minarray[i] - prev)
            prev = maxarray[i]
        
        maxgap = max(maxgap, maxx - prev)
        return maxgap
    
