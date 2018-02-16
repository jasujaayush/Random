class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        from collections import defaultdict
        count = defaultdict(int)
        for c in s:
            count[c] += 1
        
        for c in t:
            count[c] -= 1
        
        for v in count.values():
            if v!=0:
                return False
        return True
