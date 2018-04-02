class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        alphabets  = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        trans = set()
        for word in words:
            morse = ''
            for c in word:
                morse +=  alphabets[ord(c) - ord('a')]
            trans.add(morse)
        return len(trans)
        
