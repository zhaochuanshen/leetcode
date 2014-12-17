'''
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if not head or not head.next:
            return head
        numofnodes = 0
        p = head
        while p.next:
            numofnodes += 1
            p = p.next
        numofnodes += 1
        last = p
        last.next = head
        actualleft = k % numofnodes
        right = numofnodes - actualleft
        p = head
        q = head.next
        i = 0
        while i < right -1:
            p = p.next
            q = q.next
            i+= 1
        p.next = None
        return q
            
