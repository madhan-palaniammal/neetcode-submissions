class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 0

        self.left = None
        self.right = None

class LRUCache:
    def __init__(self):
        self.cache = {}

        self.oldest = Node(0, 0)
        self.newest = Node(0, 0)
        self.oldest.right = self.newest
        self.newest.left = self.oldest

    def length(self):
        return len(self.cache)

    def remove(self, node):
        if node.key not in self.cache:
            return
        
        del self.cache[node.key]

        left_node, right_node = node.left, node.right

        left_node.right = right_node
        right_node.left = left_node


    def removeLRU(self):
        lru = self.oldest.right
        self.remove(lru)
        return lru

    def insert(self, node):
        self.cache[node.key] = node.value

        left_node = self.newest.left

        self.newest.left = node
        left_node.right = node

        node.left = left_node
        node.right = self.newest

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

        # key: Node
        self.cache = {}
        self.lfuCount = 0
        self.lfuCountLRU = defaultdict(LRUCache)
    
    def update_cache(self, node):
        self.lfuCountLRU[node.freq].remove(node)
        if (
            node.freq == self.lfuCount and 
            self.lfuCountLRU[self.lfuCount].length() == 0
        ):
            self.lfuCount += 1

        node.freq += 1
        self.lfuCountLRU[node.freq].insert(node)
        self.lfuCount = min(node.freq, self.lfuCount)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.update_cache(self.cache[key])
        return self.cache[key].value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
        else:
            node = Node(key, value)
            if len(self.cache) == self.capacity:
                lfu = self.lfuCountLRU[self.lfuCount].removeLRU()
                del self.cache[lfu.key]
        
        self.cache[key] = node
        self.update_cache(node)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)