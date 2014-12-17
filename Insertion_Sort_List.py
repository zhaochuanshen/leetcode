'''
Sort a linked list using insertion sort.
'''


class Solution:

 def insertionSortList(self, head):
    if not head:
        return head
    extrahead = ListNode(-9999999)
    extrahead.next = head
    cur = head
    while cur.next:
        if cur.next.val < cur.val:
            prev = extrahead
            while prev.next.val < cur.next.val:
                prev = prev.next
            t = cur.next
            cur.next = t.next
            t.next = prev.next
            prev.next = t
        else:
            cur = cur.next
    return extrahead.next
