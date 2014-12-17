'''
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''

class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        A = sorted(num)
        i = 0
        closediff = float("inf")
        result = float("inf")
        while i < len(A) -2:
            j, k = i+1, len(A)-1
            while j < k:
                diff = A[i] + A[j] + A[k] - target
                if diff < 0:
                    if math.fabs(diff) < math.fabs(closediff):
                        closediff, result = diff, diff + target
                    j += 1
                elif diff > 0:
                    if math.fabs(diff) < math.fabs(closediff):
                        closediff, result = diff, diff + target
                    k -= 1
                else:
                    return target
            i += 1
        return result
