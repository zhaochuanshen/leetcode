'''
Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
'''
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if not root:
            return root
        stack = []
        pre = None
        stack.append(root)
        while len(stack):
            x = stack.pop()
            if pre:
                pre.left = None
                pre.right = x
            pre = x
            if x.right:
                stack.append(x.right)
            if x.left:
                stack.append(x.left)

