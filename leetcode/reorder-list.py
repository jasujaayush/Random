# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        # find center node of linked list
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        middle = slow.next
        slow.next = None
        
        # reverse list from center
        back = None
        current = middle
        while current:
            nextNode = current.next
            current.next  = back
            back = current
            current = nextNode
        #print back.val
        #print head.val
        
        t = head
        while back:
            rem_back = back.next
            back.next = t.next
            t.next = back
            t = back.next
            back = rem_back
        
        
        
            
            
