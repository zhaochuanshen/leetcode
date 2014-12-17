'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
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
    def zigzagLevelOrder(self, root):
        result = []
        if root == None:
            return result
        current = [root]
        while len(current) > 0:
            # -- None of the code above this tag up to the previous tag is actually needed -- #
                vals = []
                size = len(current)
                for i in range(size):
                    this_node = current[0]
                    vals.append(this_node.val)
                    #if i < len(current) - 1:
                        #this_node.next = current[i+1]
                    if this_node.left:
                        current.append(this_node.left)
                    if this_node.right:
                        current.append(this_node.right)
                    current.pop(0)
                result.append(vals)
        for i in xrange(len(result)):
            if i % 2 ==1:
                result[i].reverse()
        return result
