# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        
        level = [root]
        while level:
            next_level = []
            level += [None]
            for i, node in enumerate(level[:-1]):
                node.next = level[i+1]
                next_level += [child for child in (node.left, node.right) if child]
            level = next_level
        
        
        
