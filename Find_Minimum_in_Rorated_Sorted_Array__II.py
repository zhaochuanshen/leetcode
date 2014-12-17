class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        if not num:
            return None
        for i in xrange(len(num) - 1):
            if num[i + 1] < num[i]:
                return num[i+1]
        return num[0]
