'''
Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].
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
    # @return a list of strings
    def wordBreak(self, s, dict):
        @memoize
        def _wordBreak(s):
            # print(s)
            results = []
            for word in dict:
                if s == word:
                    results.append(word)
                elif s.startswith(word):
                    # print('got', word)
                    for result in _wordBreak(s[len(word):]):
                        results.append(word+' '+result)

            return results

        return _wordBreak(s)
        
