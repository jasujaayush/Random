# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        nums1 = []
        len1 = 0
        len2 = 0
        nums2 = []
        while l1:
            nums1.append(l1.val)
            len1 += 1
            l1 = l1.next
        while l2:
            nums2.append(l2.val)
            len2 += 1
            l2 = l2.next
        
       
        for _ in range(len1 - len2): nums2.insert(0,0)
        for _ in range(len2 - len1): nums1.insert(0,0)
        
        
        s = [0]*(len(nums1)+1)
        for i in range(len(nums1)-1, -1, -1):
            val = nums1[i] +  nums2[i] + s[i+1]
            s[i+1] = val%10
            s[i] = val/10
        #print nums1, nums2, s
        final = ListNode(0)
        temp = final
        for n in s:
            temp.next = ListNode(n)
            temp = temp.next
        
        while final and final.next and final.val == 0:
            final = final.next
        return final
            
        
        
        
        
