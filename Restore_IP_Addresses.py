'''
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
'''
class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        def validSegment(string):
            if len(string) == 0 or str(int(string)) != string or int(string) > 255:
                return False
            return True
        
        result = []
        for i in xrange(1, min(len(s)-2, 4)):
            for j in xrange(i+1, min(len(s)-1, i+4)):
                for k in xrange(j+1, min(len(s), j+4)):
                    if validSegment(s[:i]) and validSegment( s[i:j]) and validSegment( s[j:k] ) and validSegment( s[k:]):
                        result.append(s[:i] +'.' + s[i:j] + '.' + s[j:k] + '.' + s[k:])
        return result
            
        
