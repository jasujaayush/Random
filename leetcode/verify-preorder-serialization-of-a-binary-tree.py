class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        def traverse(vals):
            global result
            if len(vals) == 0:
                return vals, False
            
            x = vals[0]
            vals = vals[1:]
            if x != '#':
                vals, left  = traverse(vals)
                vals, right = traverse(vals)
                return vals, (left and right)
            return vals, True
        vals = preorder.split(',')
        vals, result = traverse(vals)
        #print vals, result
        return result and len(vals) == 0
        
