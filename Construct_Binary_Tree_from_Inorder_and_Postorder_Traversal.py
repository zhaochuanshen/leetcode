'''
Given inorder and postorder traversal of a tree, construct the binary tree.

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
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTreeHelper(self, d, inorder, instart, inend, postorder, poststart, postend):
        if instart > inend or poststart > postend:
            return None
        v = postorder[postend]
        root = TreeNode(x = v )
        index = d[v]
        leftsize = index - instart
        root.left = self.buildTreeHelper(d, inorder, instart, index-1, postorder, poststart, poststart+leftsize-1)
        root.right = self.buildTreeHelper(d, inorder, index+1, inend, postorder, poststart+leftsize, postend-1)
        return root
    
    def buildTree(self, inorder, postorder):
        d = {}
        size = len(inorder)
        for i in xrange(size):
            d[inorder[i]] = i
        root = self.buildTreeHelper(d, inorder, 0, size-1, postorder, 0, size-1)
        return root
