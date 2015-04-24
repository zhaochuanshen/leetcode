'''
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

For example:
Given the following binary tree,
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
You should return [1, 3, 4].
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
    def rightSideView(self, root):
        if not root:
            return []
        res = []
        stack = [root]
        while len(stack) > 0:
            l = len(stack)
            for i in xrange(l):
                x = stack.pop(0)
                if i == l-1:
                    res.append(x.val)
                if x.left:
                    stack.append(x.left)
                if x.right:
                    stack.append(x.right)
        return res
        
        
