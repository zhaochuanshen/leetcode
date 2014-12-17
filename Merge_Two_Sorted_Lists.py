'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#import sys

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
            
        if l1.val < l2.val:
            temp = self.mergeTwoLists(l1.next, l2)
            l1.next = temp
            return l1
        else:
            temp = self.mergeTwoLists(l1, l2.next)
            l2.next = temp
            return l2
