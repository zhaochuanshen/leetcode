'''
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTreeHelper(self, d, preorder, inorder, in_s, in_e, pre_s, pre_e):
        if in_s > in_e or pre_s > pre_s:
            return None
        v = preorder[pre_s]
        root = TreeNode(x = v)
        index = d[v]
        leftsize = index - in_s
        root.left = self.buildTreeHelper(d, preorder, inorder, in_s, index-1, pre_s+1, pre_s + leftsize )
        root.right = self.buildTreeHelper(d, preorder, inorder, index + 1, in_e, pre_s + leftsize + 1, pre_e)
        return root
    
    def buildTree(self, preorder, inorder):
        d = {}
        s = len(preorder)
        for i in xrange(s):
            d[inorder[i]] = i
        root = self.buildTreeHelper(d, preorder, inorder, 0, s-1, 0, s-1)
        return root
    
    
