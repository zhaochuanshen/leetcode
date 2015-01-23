'''
Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.
'''


class Solution:
    # @return a boolean
    def isScramble(self, s1, s2):
        cache = {}
        def _isScramble(s1, s2): #if this function is called, s1 and s2 are permutations of each other
            try:
                return cache[(s1, s2)]
            except KeyError:
                if s1 == s2:
                    cache[(s1, s2)] = True
                    return True
                if sorted(s1) != sorted(s2):
                    cache[(s1, s2)] = False
                    return False
                for i in xrange(1,len(s1)):
                    x = (_isScramble(s1[:i], s2[:i])  and _isScramble(s1[i:], s2[i:])  ) \
						or (_isScramble(s1[:i], s2[-i:])  and _isScramble(s1[i:], s2[:-i]) )
                    if x:
                        cache[(s1, s2)] = x
                        return x
                cache[(s1, s2)] = False
                return False
        if len(s1) != len(s2) or sorted(s1) != sorted(s2):
            return False
        return _isScramble(s1, s2)
