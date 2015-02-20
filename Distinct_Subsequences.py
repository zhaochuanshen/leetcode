'''
Given a string S and a string T, count the number of distinct subsequences of T in S.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.
'''



class Solution:
    # @return an integer
    def numDistinct(self, S, T):
        dp = [[0 for j in xrange(len(S) + 1)] for i in xrange(len(T) + 1)]
        for i in xrange( len(T) + 1):
            dp[i][0] = 0
        for i in xrange(len(S) + 1):
            dp[0][i] = 1
        for i in xrange(1, len(T) + 1 ):
            for j in xrange(1, len(S) + 1):
                if S[j-1] != T[i-1]:
                    dp[i][j] = dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
        return dp[-1][-1]
