# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def merge(self, l1, l2):
        if not l1:
            return l2
        
        if not l2:
            return l1
        
        head = cur = ListNode(0)
        while l1 and l2:
            if l1.val > l2.val:
                cur.next, l2 = l2, l2.next
            else:
                cur.next, l1 = l1, l1.next 
            cur = cur.next  
        cur.next = l1 if l1 else l2
        return head.next
                
            
    
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: 
            return head
        
        slow = fast = head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None
        
        l1 = self.sortList(slow)
        l2 = self.sortList(head)
        return self.merge(l1, l2)
        
