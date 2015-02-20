'''
mplement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
'''



class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        cache = {}
        def _isMatch(s, p):
            try:
                return cache[(s, p)]
            except:
                if not p:
                    return not s
                if p[-1] == '*':
                    if _isMatch(s, p[:-2]):
                        cache[(s, p)] = True
                        return True
                    if s and (s[-1] == p[-2] or p[-2] == '.') and _isMatch(s[:-1], p): # p match s[0:-1]
                        cache[(s, p)] = True
                        return True
                if s and (s[-1] == p[-1] or p[-1] == '.') and _isMatch(s[:-1], p[:-1]): 
                    cache[(s, p)] = True
                    return True
                cache[(s, p)] = False
                return False
        return _isMatch(s, p)
