'''
Given an array of strings, return all groups of strings that are anagrams.

Note: All inputs will be in lower-case.
'''

class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        c = {}
        for s in strs:
            try:
                c[tuple(sorted(s))] += 1
            except:
                c[tuple(sorted(s))] = 1
        return filter(lambda x: c[tuple(sorted(x))] > 1, strs)
