class Trie:

    def __init__(self):
        self.leaf = {}
        self.isEnd = False

    def insert(self, word: str) -> None:
        if word:
            letter = word[0]
            if letter not in self.leaf:
                self.leaf[letter] = Trie()
            self.leaf[letter].insert(word[1:])
        else:
            self.isEnd = True
        

    def search(self, word: str) -> bool:
        if not word:
            return self.isEnd
        if word[0] not in self.leaf:
            return False
        return self.leaf[word[0]].search(word[1:])
        

    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return True
        if prefix[0] not in self.leaf:
            return False
        return self.leaf[prefix[0]].startsWith(prefix[1:])
        
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)