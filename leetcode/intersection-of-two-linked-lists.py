# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        tempA = headA
        tempB = headB
        lenA = 0
        while tempA:
            lenA += 1
            tempA = tempA.next
        lenB = 0
        while tempB:
            lenB += 1
            tempB = tempB.next    
        
        tempA = headA
        tempB = headB
        for _ in range(lenA-lenB): tempA = tempA.next
        for _ in range(lenB-lenA): tempB = tempB.next
        
        while tempA and tempB and tempA != tempB:
            tempA = tempA.next
            tempB = tempB.next
        return tempA
        
