# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if t == None:
            return ""
        else:
            r = str(t.val)
            if t.right!=None:
                r += "(" +self.tree2str(t.left) + ")" + "(" +self.tree2str(t.right) + ")"
            elif t.left != None:
                r += "(" +self.tree2str(t.left) + ")" 
            return r
