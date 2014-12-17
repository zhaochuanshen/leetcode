'''
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
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
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        res = []
        current = []
        k = 0
        return self.pathSumHelper(root,sum, res, current, k)
        
    
    def pathSumHelper(self, root, sum, res, current, k):
        if not root:
            return res
    
        if root.val + k == sum and not root.left and not root.right:
            #current.append(root.val)
            #res.append(current)
            return res + [current + [root.val]]
            
        return self.pathSumHelper(root.left, sum, res, current +[root.val], k+root.val) + self.pathSumHelper(root.right, sum, res, current +[root.val], k+root.val)
        
