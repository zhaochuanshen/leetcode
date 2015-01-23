'''
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.
'''


class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        #this problem is very similar to edit distance
        if len(s1) + len(s2) != len(s3):
            return False
        lookup = [[False for j in xrange(len(s2) +1)] for i in xrange(len(s1) + 1)]
        for i in xrange(0, len(s1) + 1):
            for j in xrange(0, len(s2) + 1):
                if i == 0 and j == 0:
                    lookup[0][0] = True
                    continue
                '''
                # these 5 lines are helpful to understand the algorithm, but not necessary
                if j == 0:
                    lookup[i][0] = (lookup[i-1][0] and s1[i-1] == s3[i-1] )
                elif i == 0:
                    lookup[0][j] = lookup[0][j-1] and s2[j-1] == s3[j-1]
                    continue
                else:
                '''
                lookup[i][j] = (lookup[i][j-1] and s2[j-1] == s3[i+j-1] )  or (lookup[i-1][j] and s1[i-1] == s3[i+j-1])
        return lookup[-1][-1]
