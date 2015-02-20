'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''

class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        def _reverse(start, end):
            while start <  end:
                num[start], num[end] = num[end], num[start]
                start += 1
                end -= 1
                
        length = len(num)
        if length < 2:
            return num
        for i in reversed( xrange(0, length-1) ):
            if num[i] < num[i+1]:
                break
        if i == 0 and num[0] > num[1]:
            _reverse(0, length-1)
            return num
        for j in reversed(xrange(1+i, length)):
            if num[j] > num[i]:
                break
        num[i], num[j] = num[j], num[i]
        _reverse(i+1, length-1)
        return num
