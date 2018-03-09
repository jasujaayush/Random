# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        result = []
        level = [root]
        while len(level):
            temp = []
            maxima = level[0].val
            for node in level:
                if node.val > maxima:
                    maxima = node.val
                temp = temp + [n for n in (node.left, node.right) if n]
            result.append(maxima)
            level = temp
        return result
