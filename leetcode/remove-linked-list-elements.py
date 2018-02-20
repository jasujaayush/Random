# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head and head.val == val:
            head = head.next
        if not head:
            return head
            
        pre = head
        nex = head.next
        while nex:
            if nex.val == val:
                pre.next = nex.next
                nex = nex.next
            else:
                pre, nex = pre.next, nex.next
        return head
        
        
        
