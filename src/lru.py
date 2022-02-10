from pprint import pprint

class LRUCache:
    def __init__(self, capacity: 'int'):
        self.capacity = capacity
        self.items = dict()
        

    def get(self, key: 'int') -> 'int':
        if key in self.items:
            item = self.items[key]
            del self.items[key]
            self.items[key] = item
            return item
        else:
            return -1
        

    def put(self, key: 'int', value: 'int') -> 'None':
        if key in self.items:
            del self.items[key]
        if len(self.items) == self.capacity:
            k = next(iter(self.items.keys()))
            del self.items[k]
        self.items[key] = value

lru=LRUCache(3)
lru.put('1','1')
lru.put('2','2')
lru.put('3','3')
print(lru.get('1'))
lru.put('4','4')
pprint(lru.items)
print(lru.get('3'))
lru.put('5','5')
pprint(lru.items)
lru.put('1','1')
pprint(lru.items)
lru.put('5','5')
print(lru.get('1'))
print(lru.get('3'))
pprint(lru.items)


