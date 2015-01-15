'''

Compare two version numbers version1 and version1.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37
'''

class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        if version1 == version2:
            return 0
        v1 = version1.split('.')
        v2 = version2.split('.')
        i = 0
        while i < min (len(v1), len(v2)):
            if int(v1[i]) < int(v2[i]):
                return -1
            elif int(v1[i]) > int(v2[i]):
                return 1
            else:
                i += 1
        if i ==  len(v1)  and i < len(v2):
            for j in xrange(i, len(v2)):
                if int(v2[j]) != 0:
                    return -1
        if  i ==  len(v2)  and i < len(v1):
            for j in xrange(i, len(v1)):
                if int(v1[j]) != 0:
                    return 1
        return 0
        
        
