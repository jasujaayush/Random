# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root, maxNode = None, minNode = None):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        if (maxNode and root.val >= maxNode.val) or (minNode and root.val <= minNode.val):
            return False
        
        return self.isValidBST(root.left, root, minNode) and self.isValidBST(root.right, maxNode, root)
        
