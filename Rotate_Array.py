'''
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
'''
class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        if not nums:
            return
        def _reverselist(s,e):
            nums[s:e] = nums[s:e][::-1]
        k = k % len(nums)
        firstend = len(nums)-k
        _reverselist(0,firstend)
        _reverselist(firstend,len(nums))
        _reverselist(0,len(nums))
