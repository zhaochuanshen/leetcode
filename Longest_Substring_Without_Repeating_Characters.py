'''
Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.
'''


class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        d = {}
        start  = 0
        result = 0
        for i, c in enumerate(s):
            try:
                if d[c] >= start:
                    start = d[c] + 1
            except: pass
            d[c] = i
            result = max(result, i+1 -start)
        return result
