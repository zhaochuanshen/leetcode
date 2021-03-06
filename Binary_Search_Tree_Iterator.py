'''
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
'''




# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stack = []
        p = root
        self.pushAll(p)
        

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return not len(self.stack) == 0

    # @return an integer, the next smallest number
    def next(self):
        x = self.stack.pop()
        self.pushAll(x.right)
        return x.val
        
    def pushAll(self, node):
        while node:
            self.stack.append(node)
            node = node.left
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
