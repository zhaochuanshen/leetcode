'''
Write a function to find the longest common prefix string amongst an array of strings.
'''

class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if len(strs) == 1:
            return strs[0]
        if not strs:
            return ''
        l = []
        for x in strs:
            l.append(len(x))
        minlen = min(l)
        lastpossible = ''
        for i in xrange(minlen):
            pre = strs[0][:i+1]
            for x in strs:
                if x[:i+1] != pre:
                    break
            if x[:i+1] != pre:
                break
            lastpossible = pre
        return lastpossible       
                
