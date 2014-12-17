'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        x = self.check(root)
        if x == -1:
            return False
        else:
            return True
    
    def check(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        
        lH = self.check(root.left)
        if lH == -1:
            return -1
        rH = self.check(root.right)
        if rH == -1:
            return -1
        dif = abs(rH - lH)
        if dif >= 2:
            return -1
        return max(rH+1, lH+1)
        
