'''
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

For example,
Given height = [2,1,5,6,2,3],
return 10.

'''

class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        s = []
        maxarea = 0
        i = 0
        while i < len(height):
            if len(s) == 0 or height[ s[-1] ]<= height[i]:
                s.append(i)
                i += 1
            else:
                tp = s.pop()
                currentarea = height[tp] * (i if len(s) == 0 else i - s[-1] -1)
                maxarea = max(maxarea, currentarea)
        
        while len(s) > 0:
            tp = s.pop()
            currentarea = height[tp] * (i if len(s) == 0 else i - s[-1] -1)
            maxarea = max(maxarea, currentarea)
        
        return maxarea
