"""
What is the longest word you can build in a game of Scrabble one letter at a time? That is, starting with a valid two-letter word, how long a word can you build by playing one letter at a time on either side to form a valid three-letter word, then a valid four-letter word, and so on?

For example:
Input dictionary: "at", "hat", "chat", "chats", "rat", "rate", "orange", "ran", "an"
Output: "chats"

at -> hat -> chat -> chats
an -> ran


A list of lowercase words is available at https://d2i1pl9gz4hwa7.cloudfront.net/7HvykrqVNLAyrVQATa9iBA
"""
import urllib;

words = urllib.urlopen("https://d2i1pl9gz4hwa7.cloudfront.net/7HvykrqVNLAyrVQATa9iBA").read().split()

#words = ["at", "hat", "chat", "chats", "chaty","rat", "rate", "orange", "ran", "an"]
queue = []
hash_map = {}
unique_words = set(words)
for word in unique_words: #assuming words have single letter words
    #hash_map[word] = True #word is present
    if len(word) == 2:
        queue.append((word,word)) #word history(index 1) is word itself

while queue:
    new_words = set()
    for word,hist in queue: #Try adding a character
        for c in 'abcdefghijklmnopqrstuvwxyz':
            if c+word in unique_words: 
                new_words.add((c+word , hist + "->" + c+word))
            if word+c in unique_words: 
                new_words.add((word+c, hist + "->" + word+c))
    if len(new_words)>0:
        queue = list(new_words)
    else:
        break

print queue if queue else '' # no word

    
        
