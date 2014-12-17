'''
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverse(self, head):
        if not head or not head.next:
            return head
        prev = None
        c = head
        while c:
            nn = c.next
            c.next = prev
            prev = c
            c = nn
        return prev
            
    def reverseBetween(self, head, m, n):
        dummy = ListNode(x = -999)
        dummy.next  = head
        t = dummy
        num = 0
        while num < m:
            s = t
            t = t.next
            num += 1
        beforem = s
        atm = t
        while num < n:
            t = t.next
            num += 1
        atn = t
        aftern = t.next
        
        atn.next = None
        beforem.next = self.reverse(atm)
        atm.next = aftern
        
        return dummy.next
        
        
