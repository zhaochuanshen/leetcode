'''
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a tree node
    def recoverTree(self, root):
        if not root:
            return root
        current = root
        before = None
        found = False
        
        while current != None:
            if current.left == None:
                #res.append(current.val)
                if before and before.val > current.val:
                    if not found:
                        f1 = before
                        found = True
                    f2 = current
                before = current
                current = current.right
            else:
                pre = current.left
                while pre.right and pre.right != current:
                    pre = pre.right
                if not pre.right:
                    pre.right = current
                    current = current.left
                else:
                    pre.right = None
                    if before.val > current.val:
                        if not found:
                            f1 = before
                            found = True
                        f2 = current
                    before = current
                    current = current.right
        f1.val, f2.val = f2.val, f1.val
        return root
        
