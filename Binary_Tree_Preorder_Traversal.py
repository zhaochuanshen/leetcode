'''
Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
       \
	        2
			    /
				   3
				   return [1,2,3].
'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        returnlist = []
        if not root:
            return returnlist
        stack = []
        stack.append(root)
        #returnlist.append(root.val)
        
        while len(stack) > 0:
            x = stack.pop()
            #returnlist.append(x.val)
            if  x.right:
                stack.append(x.right)
            if x.left:
                stack.append(x.left)
            returnlist.append(x.val)
        return returnlist
