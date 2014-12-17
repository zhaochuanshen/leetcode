'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        result = []
        if root == None:
            return result
        queue = [root]
        while len(queue) > 0:
            # -- None of the code above this tag up to the previous tag is actually needed -- #
                current = []
                size = len(queue)
                for i in range(size):
                    x = queue.pop(0)
                    current.append(x.val)
                    #if i < len(current) - 1:
                        #this_node.next = current[i+1]
                    if x.left:
                        queue.append(x.left)
                    if x.right:
                        queue.append(x.right)
                    
                result.append(current)
        return result
