#
# @lc app=leetcode.cn id=460 lang=python3
#
# [460] LFU 缓存
#

# @lc code=start

from collections import defaultdict
from typing import Dict


class Node:
    def __init__(self, key: int, value: int, freq: int = 1, prev = None, next = None):
        self.key = key
        self.value = value
        self.freq = freq
        self.prev = prev
        self.next = next


class DLL:
    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next, self.tail.prev = self.tail, self.head
        self.size = 0

    def appendNode(self, node: Node):
        tail = self.tail.prev
        assert tail is not None
        self.tail.prev = tail.next = node
        node.prev, node.next = tail, self.tail
        self.size += 1

    def removeNode(self, node: Node):
        assert node.prev is not None
        assert node.next is not None
        node.prev.next, node.next.prev = node.next, node.prev
        self.size -= 1

    def shiftNode(self):
        if self.size:
            node = self.head.next
            assert node is not None
            self.removeNode(node)
            return node
        return None


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache: Dict[int, Node] = {}
        self.store = defaultdict(DLL)
        self.minFreq = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.increaseFreq(node)
        return node.value

    def increaseFreq(self, node: Node) -> None:
        freq = node.freq
        node.freq = freq + 1
        self.store[freq].removeNode(node)
        self.store[node.freq].appendNode(node)
        if freq == self.minFreq and not self.store[freq].size:
            self.minFreq = node.freq    

    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.increaseFreq(node)
        elif self.ensure(self.minFreq):
            node = Node(key, value)
            self.cache[key] = node
            self.store[node.freq].appendNode(node)
            self.minFreq = 1
    
    def ensure(self, freq):
        if not self.capacity:
            return False
        if len(self.cache) < self.capacity:
            return True
        item = self.store[freq].shiftNode()
        assert item is not None
        del self.cache[item.key]
        return True       

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
