# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def inorder(node):
            result = []
            if node:
                result =  inorder(node.left) + [node.val] + inorder(node.right)
            return result
        
        vals = inorder(root)
        return min([vals[i+1]-vals[i] for i in range(len(vals)-1)])
