# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePathInternal(self, root, val):
        if (not root) or root.val != val:
            return 0
        return 1 + max(self.longestUnivaluePathInternal(root.left, val), self.longestUnivaluePathInternal(root.right, val))
    
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        max_val = max(self.longestUnivaluePath(root.left), self.longestUnivaluePath(root.right))
        max_val = max(max_val,self.longestUnivaluePathInternal(root.left, root.val) + self.longestUnivaluePathInternal(root.right, root.val))
        return max_val
        
