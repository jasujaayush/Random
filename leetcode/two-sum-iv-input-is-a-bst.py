# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def traverse(self, root):
        if not root:
            return []
        return self.traverse(root.left) + [root.val] + self.traverse(root.right)
    
    def findTarget(self, root, target):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        numbers = self.traverse(root)
        d = {}
        for n in numbers:
            if d.has_key(target-n):
                return True
            d[n] = 1
        return False
        
