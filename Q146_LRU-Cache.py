class DualLinkedList:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev
    

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = DualLinkedList(None, None)
        self.tail = DualLinkedList(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.seen = {}
    
    
    def delete_node(self, key):
        
        node = self.seen[key]
        node.next.prev = node.prev
        node.prev.next = node.next
        del self.seen[key]
        del node 
        
    def put_node(self, key, val):
        new_node = DualLinkedList(key, val, prev=self.tail.prev, next=self.tail)
        self.tail.prev.next = new_node
        self.tail.prev = new_node
        self.seen[key] = new_node

    def get(self, key: int) -> int:
        if key in self.seen:
            val = self.seen[key].val
            self.delete_node(key)
            self.put_node(key, val)
            return val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.seen:
            self.delete_node(key)
        if self.capacity == len(self.seen):
            self.delete_node(self.head.next.key)
        self.put_node(key, value)
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)