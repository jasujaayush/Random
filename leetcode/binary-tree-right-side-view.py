# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        
        res = []
        level = [root]
        while level:
            temp = []
            for node in level:
                temp += [child for child in (node.left, node.right) if child]
            res.append(level[-1].val)
            level = temp
        return res
