'''
Implement strStr().
'''

class Solution:
    def strStr(self, haystack, needle):
        if not needle or len(needle) == 0:
            return 0
        if len(haystack) < len(needle):
            return -1
        for i in xrange(len(haystack) - len(needle) + 1):
            found = True
            for j in xrange(len(needle)):
                if haystack[i+j] != needle[j]:
                    found = False
                    break
            if found:
                return i
        return -1
