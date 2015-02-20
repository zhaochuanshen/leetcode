'''
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 10,1,2,7,6,1,5 and target 8, 
A solution set is: 
[1, 7] 
[1, 2, 5] 
[2, 6] 
[1, 1, 6] 
'''


class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        def _combinationSum2(result, li, index, target):
            if target == 0:
                result.append(li)
                return
            if candidates[-1] * (len(candidates) - index)<target:
                return
            while index < len(candidates):
                newtarget = target - candidates[index]
                if newtarget < 0:
                    return
                licopy = list(li)
                licopy.append(candidates[index])
                _combinationSum2(result, licopy, index+1, newtarget)
                temp = candidates[index]
                while index < len(candidates) and candidates[index] == temp:
                    index += 1
        
        result = []
        li = []
        candidates.sort()
        _combinationSum2(result, li, 0, target)
        return result
