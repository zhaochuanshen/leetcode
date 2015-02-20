'''
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
'''

class Solution:
    # @return a string
    def longestPalindrome(self, s):
        def _isPalindrome(start, end):
            for i in xrange(start, (start+end+1)/2):
                if s[i] != s[end + start- i]:
                    return False
            return True
            
        longest_Start = 0
        max_Length = 0
        if len(s) == 0:
            return s
        for i in xrange(len(s)):
            if _isPalindrome(i - max_Length, i ):
                longest_Start = i -max_Length
                max_Length += 1
            elif i - max_Length - 1 >=0 and _isPalindrome(i - max_Length - 1, i ):
                longest_Start = i-max_Length - 1
                max_Length += 2
        return s[longest_Start:longest_Start + max_Length]
