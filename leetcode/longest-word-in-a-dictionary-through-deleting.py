class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        d.sort()
        ans = ''
        for word in d:
            wi = 0
            si = 0
            while si < len(s) and wi < len(word):
                if s[si] == word[wi]:
                    wi+=1
                    if wi == len(word) and wi > len(ans):
                        ans = word
                si+=1
        return ans
        
