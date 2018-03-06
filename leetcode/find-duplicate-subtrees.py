# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        compressed = collections.defaultdict(list)
        def serialize(root):
            data = ''
            if root:
                data = data + str(root.val)
                l = serialize(root.left)
                r = serialize(root.right)
                data = data + " " + l + " " + r
            else:
                data = '#'
            compressed[data].append(root)
            return data
        serialize(root)
        
        results = []
        for key in compressed:
            val = compressed[key]
            if key != '#' and len(val) > 1:
                results.append(val[0])
        return results
