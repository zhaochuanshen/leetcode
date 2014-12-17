
'''
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        if not head:
            return None
        if not head.next:
            root = TreeNode(head.val)
            return root
        if not head.next.next:
            root = TreeNode(head.next.val)
            leaf = TreeNode(head.val)
            root.left = leaf
            return root
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        t = head
        
        while t.next != slow:
            t = t.next
        
        t.next = None
        
        root = TreeNode(slow.val)

        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        return root
        
