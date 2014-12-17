'''
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head
        newhead = ListNode(-99999999999)
        newhead.next = head
        p = newhead
        while p and p.next:
            q = p.next
            while q.next and q.next.val == q.val:
                q = q.next
            if p.next ==q:
                p = q
            else:
                p.next = q.next
            
        return newhead.next
        
        
