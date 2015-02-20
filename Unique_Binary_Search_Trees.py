'''
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''




class Solution:
    # @return an integer
    def numTrees(self, n):
        result = [1,1,2]
        if n <= 2:
            return result[ n]
            
        for i in xrange(3, n+1):
            temp = 0
            for k in xrange(1, i+1):
                temp += result[i-k] * result[k-1]
            result.append(temp)
        return result[-1]
        
