# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        temp = root
        length = 0
        while temp:
            length+=1
            temp = temp.next
            
        part_length = length/k
        remains = length%k
        
        parts = [part_length+1]*remains + [part_length]*(k-remains)
        
        results = []
        temp = root
        for l in parts:
            res = []
            while temp and len(res)<l:
                res.append(temp.val)
                temp = temp.next
            results.append(res)
        return results
        
