import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data_dict = {}
        self.data_list = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.data_dict:
            self.data_dict[val] = len(self.data_list)
            self.data_list += [val]
            return True
        return False
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.data_dict:
#             swap the storing index in data dict
            self.data_dict[self.data_list[-1]] = self.data_dict[val]
#             swap the storing index in data list            
            self.data_list[self.data_dict[val]], self.data_list[-1] = self.data_list[-1], self.data_list[self.data_dict[val]]
            
            del self.data_dict[val]
            del self.data_list[-1]
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.data_list[random.randint(0, len(self.data_list)-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()