'''
Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [3,2,1].
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
    def postorderTraversal(self, root):
        stack1 = []
        stack2 = []
        if not root:
            return stack1
        stack1.append(root)
        while len(stack1) >0:
            current = stack1.pop()
            stack2.append(current.val)
            if current.left:
                stack1.append(current.left)
            if current.right:
                stack1.append(current.right)
        stack2.reverse()
        return stack2
