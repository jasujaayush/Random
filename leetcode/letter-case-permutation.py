class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        S = S.lower()
        results = set([S])
        for i,c in enumerate(S):
            if c in 'abcdefghijklmnopqrstuvwxyz':
                new = []
                for r in results:
                    new += [r[:i] + c.upper() + r[i+1:], r[:i] + c + r[i+1:]]
                results = results.union(new)
        
        return list(results)
