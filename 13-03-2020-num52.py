# LRU cache implementation

class Node:
    def __init__(self, val, prev, nex):
        self.previous = prev
        self.next = nex
        self.value = val

class LRUCache:
    def __init__(self, n):
        self.cache_size = n
        self.last = None
        self.first = None
        self.cache = {}

    def set(self, key, value):
        if len(self.cache) < self.cache_size or key in self.cache:
            if self.last == None: # If cache is empty
                self.cache[key] = Node(value, None, None)
                self.last = key
                self.first = key
            else:
                if key not in self.cache:
                    self.cache[key] = Node(value, self.last, None)
                    self.cache[self.last].next = key
                    self.last = key
                else:
                    if key != self.last:
                        if self.cache[key].previous != None:
                            self.cache[self.cache[key].previous].next = self.cache[key].next
                        else: # if first == key
                            self.first = self.cache[key].next
                        self.cache[self.cache[key].next].previous = self.cache[key].previous
                        self.cache[self.last].next = key
                        self.cache[key].previous = self.last
                        self.cache[key].next = None
                        self.last = key
                    else:
                        self.cache[self.last].value = value
        else:
            tmp = self.cache[self.first].next
            del self.cache[self.first]
            self.first = tmp
            self.cache[key] = Node(value, self.last, None)
            self.cache[self.last].next = key
            last = key

    def get(self, key):
        if key not in self.cache: # O(1) because dicts are hashmaps
            return None
        else:
            if key != self.last:
                if self.cache[key].previous != None:
                    self.cache[self.cache[key].previous].next = self.cache[key].next
                else: # if first == key
                    self.first = self.cache[key].next
                self.cache[self.cache[key].next].previous = self.cache[key].previous

                self.cache[self.last].next = key
                self.cache[key].previous = self.last
                self.cache[key].next = None
                self.last = key
            return self.cache[key].value
#Tests
disk = LRUCache(4)
disk.set("lol", 3)
print("lol value: " + str(disk.get("lol")))
disk.set("mdr", 6)
disk.set("fun", 7)
disk.set("lmao", 1)
print("mdr value: " + str(disk.get("mdr")))
disk.set("kaba", 9)
disk.set("lmao", 8)
