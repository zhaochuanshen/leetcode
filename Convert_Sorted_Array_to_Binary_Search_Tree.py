'''
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        if not num:
            return None
        if len(num) == 1:
            node = TreeNode(num[0])
            return node
        if len(num) == 2:
            root = TreeNode(num[1])
            leaf = TreeNode(num[0])
            root.left = leaf
            return root
        N = len(num)
        root = TreeNode(num[N/2])
        root.left = self.sortedArrayToBST(num[:N/2])
        root.right = self.sortedArrayToBST(num[N/2 + 1:])
        return root
        
        
