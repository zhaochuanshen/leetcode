'''
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:
Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
The solution set must not contain duplicate quadruplets.
    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)

'''


class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        num.sort()
        length = len(num)
        result = []
        s = 0
        while s < length:
            e = length-1
            while e >= s +3:
                i = s + 1
                j = e - 1
                while i < j:
                    if num[i] + num[j] + num[s] + num[e] < target:
                        i += 1
                    elif num[i] + num[j] + num[s] + num[e] > target:
                        j -= 1
                    else:
                        result.append([num[s], num[i], num[j], num[e]])
                        i += 1
                        j -= 1
                        while i < j and num[j+1] == [j]:
                            j -= 1
                        while i < j and num[i-1] == num[i]:
                            i += 1
                e -= 1
                while e >= s+3 and num[e+1] == num[e]:
                    e -= 1
            s += 1
            while s < length and num[s-1] == num[s]:
                s += 1
        return result
        
