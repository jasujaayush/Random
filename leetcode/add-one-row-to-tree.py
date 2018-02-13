# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, root, current_depth, v, d):
        if not root:
            return
        
        if current_depth == d - 1:
            node1 = TreeNode(v)
            if root:
                node1.left = root.left
                root.left = node1
            
            node2 = TreeNode(v)
            if root:
                node2.right = root.right
                root.right = node2
        else:
            self.helper(root.right, 1+current_depth, v, d)
            self.helper(root.left, 1+current_depth, v, d)
            
    
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            node = TreeNode(v)
            node.left = root
            return node
          
        self.helper(root, 1, v, d)
        return root
        
