"""
https://leetcode.com/problems/design-hashmap/

Design a HashMap without using any built-in hash table libraries.

To be specific, your design should include these functions:

put(key, value) : Insert a (key, value) pair into the HashMap. 
If the value already exists in the HashMap, update the value.

get(key): Returns the value to which the specified key is mapped, 
or -1 if this map contains no mapping for the key.

remove(key) : Remove the mapping for the value key if this map 
contains the mapping for the key.

Example:

hashMap = MyHashMap()
hashMap.put(1, 1)          
hashMap.put(2, 2)         
hashMap.get(1)            // returns 1
hashMap.get(3)            // returns -1 (not found)
hashMap.put(2, 1)          // update the existing value
hashMap.get(2)            // returns 1 
hashMap.remove(2)          // remove the mapping for 2
hashMap.get(2)            // returns -1 (not found) 

Note:

All keys and values will be in the range of [0, 1000000].
The number of operations will be in the range of [1, 10000].
Please do not use the built-in HashMap library.
"""


class ListNode:
    def __init__(self, key, value):
        self.next = None
        self.key = key
        self.value = value


class MyHashMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.len = 1000
        self.table = [None for i in range(self.len)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hashcode = key % self.len
        if self.table[hashcode] is None:
            self.table[hashcode] = ListNode(key, value)
        else:
            node = self.table[hashcode]
            while True:
                if node.key == key:
                    node.value = value
                    break
                elif node.next is None:
                    node.next = ListNode(key, value)
                    break
                else:
                    node = node.next

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, 
        or -1 if this map contains no mapping for the key
        """
        hashcode = key % self.len
        if self.table[hashcode] is None:
            return -1
        else:
            node = self.table[hashcode]
            while node:
                if node.key == key:
                    return node.value
                node = node.next
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key 
        if this map contains a mapping for the key
        """
        hashcode = key % self.len
        if self.table[hashcode] is None:
            return
        else:
            node = self.table[hashcode]
            if node.key == key:
                self.table[hashcode] = node.next
                return
            while node.next:
                if node.next.key == key:
                    node.next = node.next.next
                    return
                node = node.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
