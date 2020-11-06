"""
https://leetcode.com/problems/lru-cache/

Design a data structure that follows the constraints 
of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

    LRUCache(int capacity): Initialize the LRU cache 
    with positive size capacity.

    int get(int key): Return the value of the 
    key if the key exists, otherwise return -1.

    void put(int key, int value): Update the value of 
    the key if the key exists. Otherwise, add the 
    key-value pair to the cache. If the number of 
    keys exceeds the capacity from this operation, 
    evict the least recently used key.

Follow up:
Could you do get and put in O(1) time complexity?

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4

Constraints:
    1 <= capacity <= 3000
    0 <= key <= 3000
    0 <= value <= 104
    At most 3 * 104 calls will be made to get and put.
"""

class Node:
    def __init__(self, key, val):
        self.next = None
        self.prev = None
        self.key = key
        self.val = val

class LRUCache:

    # head.next: most recently used
    # tail.prev: least recently used
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        # dummy nodes
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # remove, so we can add again
            # so that it appears most recently used
            self.__remove(node)
            self.__add_front(node)
            return node.val
        return -1
        
    def put(self, key: int, value: int) -> None:
        # updating the key if it already exists,
        # is the same as removing it and adding the
        # new node
        if key in self.cache:
            self.__remove(self.cache[key])
        node = Node(key, value)
        self.__add_front(node)
        self.cache[key] = node
        # Just remove the lru "least recently used"
        # which in this implementation is self.tail.prev
        if len(self.cache) > self.capacity:
            node = self.tail.prev
            self.__remove(node)
            del self.cache[node.key]
        
    # Removes the given node
    def __remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    # Adds given node to head (makes it MRU "most recently used")
    def __add_front(self, node):
        node.next = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next.prev = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)