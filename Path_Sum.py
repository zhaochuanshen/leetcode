'''
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
'''
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if not root:
            return False
        k = 0
        return self.hasPathSumHelper(root, sum, k)
        
    def hasPathSumHelper(self, root, sum, k):
        if not root:
            return False
        if not root.left and not root.right:
            if root.val + k == sum:
                return True
            else:
                return False
        return self.hasPathSumHelper(root.left, sum, k+ root.val) or self.hasPathSumHelper(root.right, sum, k+ root.val)
