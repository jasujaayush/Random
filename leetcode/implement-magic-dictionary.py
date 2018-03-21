class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.orig = set()
        self.words = {}

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for word in dict:
            self.orig.add(word)
            for i in range(len(word)):
                t = word[:i] + '*' + word[i+1:]
                self.words[t] = self.words.get(t,0) + 1
        

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        for i in range(len(word)):
            t = word[:i] + '*' + word[i+1:]
            if (self.words.get(t,0) > 1) or (t in self.words and word not in self.orig):
                return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
