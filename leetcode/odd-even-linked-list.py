# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy1 = odd = ListNode(0)
        dummy2 = even = ListNode(0)
        dummy = odd
        while head:
            odd.next = head
            even.next = head.next
            odd = odd.next
            even = even.next
            if even:
                head = head.next.next
            else:
                head = None
        odd.next = dummy2.next
        return dummy1.next
        
