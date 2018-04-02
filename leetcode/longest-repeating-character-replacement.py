class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        chars = {}
        total = 0
        maxima = 0
        start = 0
        for i,c in enumerate(s):
            chars[c] = chars.get(c,0) + 1
            max_val = max(chars.values())
            other_val = sum(chars.values()) - max_val
            if other_val <= k:
                maxima = max(maxima, i - start + 1)
            else:
                chars[s[start]] -= 1
                start += 1
        maxima = max(maxima, len(s) - start)
        return maxima
            
        
