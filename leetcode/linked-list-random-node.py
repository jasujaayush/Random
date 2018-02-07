# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        result = self.head.val
        node = self.head.next
        index = 1
        while node != None:
            r = random.randint(0,index)
            if r == 0: #If random lies within the window of reservoir (0 in this case), replace it with new value
                result = node.val
            index += 1
            node = node.next
        return result
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
