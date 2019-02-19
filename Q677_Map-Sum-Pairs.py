class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.letter_table = {}        
        # self.letter_table = {}
    def insert(self, key: 'str', val: 'int') -> 'None':
        if key:
            self.letter_table[key] = val
            
    def sum(self, prefix: 'str') -> 'int':
        count = 0
        for key, val in self.letter_table.items():
            if key.startswith(prefix):
                count += val
        return count

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)