'''
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".


'''
class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        l  = s.split()
        if len(l) == 0:
            return ''
        l.reverse()
        spaces = [' ' for i in xrange(len(l) - 1)]
        x = []
        for i in xrange(len(l) - 1):
            x.append(l[i])
            x.append(spaces[i])
        x.append(l[-1])
        return ''.join(x)
