class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
    
class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.hash = [None]*self.size
    
    def gethash(self, key):
        return key%self.size
    
    def add(self, key: int) -> None:
        hash_key = self.gethash(key)
        node = self.hash[hash_key]
        cur_node = Node(key)
        cur_node.next = node
        self.hash[hash_key] = cur_node
            

    def remove(self, key: int) -> None:
        hash_key = self.gethash(key)
        node = self.hash[hash_key]
        last_node = None
        while node:
            if node.key == key:
                if last_node:
                    last_node.next = node.next
                else:
                    self.hash[hash_key] = node.next
            else:
                last_node = node
            node = node.next

    def contains(self, key: int) -> bool:
        hash_key = self.gethash(key)
        node = self.hash[hash_key]
        while node:
            if node.key == key:
                return True
            node = node.next
        return False