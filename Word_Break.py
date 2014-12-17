'''
Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
'''


def memoize(function):
	memo = {}
	def wrapper(*args):
		if args in memo:
			return memo[args]
		else:
			rv = function(*args)
			memo[args] = rv
			return rv
	return wrapper

class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        
        @memoize
        def _wordBreak(s):
            if s in dict:
                return True
            for i in xrange(len(s)):
                if s[:i+1] in dict and _wordBreak(s[i+1:]):
                    return True
            return False        
        return _wordBreak(s)   
            
        
