class LRUCache:

    def __init__(self, capacity: int):
        self.count = 0
        self.capacity = capacity
        self.values = {}
        self.accesses = []
        

    def get(self, key: int) -> int:
        if key in self.values:
            self.accesses.remove(key)
            self.accesses.insert(0,key)
            return self.values[key]
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.values:
            self.values[key] = value
            self.accesses.remove(key)
            self.accesses.insert(0,key)
            return
        if self.count == self.capacity:
            self.values.pop(self.accesses.pop())
            self.count -= 1
        self.accesses.insert(0,key)
        self.values[key] = value
        self.count += 1
        

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)