# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []
        
        queue = [root]
        results = []
        while len(queue):
            newq = []
            s = 0
            for node in queue:
                s += node.val
                if node.left:
                    newq.append(node.left)
                if node.right:
                    newq.append(node.right)
            results.append(s/float(len(queue)))
            queue = newq
        return results
            
            
        
