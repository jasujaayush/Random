class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        mapping = {}
        for e in range(len(B)):
            mapping[B[e]] = e
        return [mapping[e] for e in A]
        
