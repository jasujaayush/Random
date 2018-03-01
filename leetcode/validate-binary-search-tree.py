# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = []
        pre = None
        while root or len(stack):
            if root:
                stack.append(root)
                root = root.left
            else:
                root =  stack.pop()
                if pre and pre.val >= root.val:
                    return False
                pre = root
                root = root.right
        return True
            
        
