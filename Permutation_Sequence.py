class Solution:
    # @return a string
    def getPermutation(self, n, k):
        res = []
        l = [str(i) for i in xrange(1, n+1)]
        k -= 1
        while len(res) < n:
            dig = k / math.factorial(len(l) - 1) 
            res.append(l[dig])
            k -= (dig) * math.factorial(len(l)-1)
            l.pop(dig)
        return "".join(res)
            
