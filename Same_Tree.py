'''
Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
'''


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if (not p) and (not q):
            return True
        if p and (not q):
            return False
        if q and (not p):
            return False
        if p.val != q.val:
            return False
        
        l = self.isSameTree(p.left, q.left)
        r = self.isSameTree(p.right, q.right)
        if l and r:
            return True
        else:
            return False
        
