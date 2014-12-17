'''
Sort a linked list in O(n log n) time using constant space complexity.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            head = l1
            p = l1
            l1 = l1.next
        else:
            head = l2
            p = l2
            l2 = l2.next
        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        if not l1:
            p.next = l2
        else:
            p.next = l1
        return head
    
    def sortList(self, head):
        if not head or head.next == None:
            return head
        slow = head
        fast = head
        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next
        l2 = slow.next
        slow.next = None
        l1 = head
        x1 = self.sortList(l1)
        x2 = self.sortList(l2)
        return self.mergeTwoLists(x1,x2)
