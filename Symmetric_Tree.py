'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
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
    def isSymmetric(self, root):
        if not root:
            return True
        if not root.left and not root.right:
            return True
        return self.isSym(root.left, root.right)
    
    def isSym(self, left, right):
        if not left and not right:
            return True
        if not left and right:
            return False
        if not right and left:
            return False
            
        if left.val != right.val:
            return False
        if not self.isSym(left.left, right.right):
            return False
        if not self.isSym(left.right, right.left):
            return False
        return True
