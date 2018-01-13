class LRUCache(object):
    #not O(1)
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.counter = 0
        self.key_time = {}
        self.key_value = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        self.counter += 1
        if self.key_value.has_key(key):
            self.key_time[key] = self.counter
            return self.key_value[key]
        else:
            return -1
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        self.key_value[key] = value
        self.counter += 1
        self.key_time[key] = self.counter
        if len(self.key_value) > self.capacity:
            lru_key = min(self.key_time, key=self.key_time.get)
            del self.key_value[lru_key]
            del self.key_time[lru_key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
