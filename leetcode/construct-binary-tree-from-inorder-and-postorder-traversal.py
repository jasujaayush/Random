# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) == 0:
            return None
        r = postorder[-1]
        node = TreeNode(r)
        ir = inorder.index(r)
        node.left = self.buildTree(inorder[:ir], postorder[:ir])
        node.right = self.buildTree(inorder[ir+1:], postorder[ir:-1])
        return node
        
