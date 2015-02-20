'''
Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3


'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @return a list of tree node
    def generateTrees(self, n):
        def _generateTrees(start, end):
            if start > end:
                return [None]
            temp = []
            for inte in xrange(start, end+1):
                leftlist = _generateTrees(start, inte-1)
                rightlist = _generateTrees(inte+1, end)
                for l in leftlist:
                    for r in rightlist:
                        node = TreeNode(inte)
                        node.left = l
                        node.right = r
                        temp.append(node)
            return temp
        return _generateTrees(1, n)
