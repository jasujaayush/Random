class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        d = [0]*26
        for c in magazine:
            d[ord(c) - ord('a')] += 1
        
        for c in ransomNote:
            d[ord(c) - ord('a')] -= 1
            if d[ord(c) - ord('a')] < 0:
                return False
        
        return True
        
