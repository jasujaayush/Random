class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        sentence = sentence.split()
        for i in range(len(sentence)):
            word = sentence[i]
            for w in dict:
                if word.startswith(w):
                    word = w
            sentence[i] = word
        return " ".join(sentence)
                    
