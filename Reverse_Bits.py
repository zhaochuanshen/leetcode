'''
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?

Related problem: Reverse Integer
'''
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        def _getBin(n):
            res = ""
            if n <= 1:
                return "0"*31+str(n)
            while n > 1:
                n, k = divmod(n,2)
                res = str(k) + res
            res = "1" + res
            if len(res) > 32:
                raise TypeError("n too large")
            return "0"*(32-len(res)) + res
        binarycode = _getBin(n)
        i = 1
        res = 0
        for k in binarycode:
            res += i*int(k)
            i *= 2
        return res
		
