class Codec:
    def __init__(self):
        self.count = 0
        self.map = {}
    
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        self.count += 1
        self.map[self.count] = longUrl
        return "http://tinyurl.com/" + str(self.count)
        
    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        x = int(shortUrl.split('/')[-1])
        return self.map[x]
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
