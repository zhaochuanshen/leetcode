'''
Given a binary tree, find the maximum path sum.

The path may start and end at any node in the tree.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.
'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        max_s = -float('infinity')
        l = [max_s]
        self.getSum(root, l)
        return l[0]
    def getSum(self, root, l):
        if not root:
            return 0
        left = self.getSum(root.left, l)
        right = self.getSum(root.right, l)
        c = root.val
        if left > 0:
            c += left
        if right > 0:
            c += right
        l[0] = max(l[0], c)
        if max(left, right) > 0:
            return root.val + max(left, right)
        else:
            return root.val
    
        
