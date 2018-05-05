class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        results = []
        l = [set("asdfghjkl"), set("qwertyuiop"), set("zxcvbnm")]
        for word in words:
            x = set(word.lower())
            for s in l:
                 if s.intersection(x) == x:
                    results.append(word)
                    break
        return results
