'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.

This beautiful idea is due to @tqlong
'''


class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        result = [i-1 for i in xrange(len(s) + 1)]
        for i in xrange(len(s)):
            j = 0
            while i - j >= 0 and i + j < len(s) and s[i+j] == s[i-j]:
                result[i+j+1] = min(result[i+j+1], result[i-j] +1)
                j+=1
            j = 1
            while i -j+1 >=0 and i+j < len(s) and s[i+1-j] == s[i+j]:
                result[i+j+1] = min(result[i+j+1], result[i+1-j] + 1)
                j+= 1
        return result[-1]
