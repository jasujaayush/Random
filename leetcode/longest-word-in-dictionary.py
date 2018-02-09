class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words.sort()
        possible = set([''])
        ans = ''
        for word in words:
            if word[:-1] in possible:
                possible.add(word)
                if len(word) > len(ans):
                    ans = word
        return ans
