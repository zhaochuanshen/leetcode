'''
Reorder List Total Accepted: 27686 Total Submissions: 135214 My Submissions Question Solution 
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if (head == None) or (head.next == None):
            return head
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        left = head
        right = slow.next
        slow.next = None
	    	
        prev = None
        while right:
            n = right.next
            right.next = prev
            prev = right
            right = n
	
	
        right = prev
        p = head
	
        while left and right:
            if p == left:
                left = left.next
                p.next = right
            else:
                right = right.next
                p.next = left
            p = p.next
        return head 

            
            
