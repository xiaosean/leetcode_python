class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.root
        cur, nex = [node], []
        for letter in word:
            for node in cur:
                if letter == '.':
                    nex += list(node.children.values())
                elif letter in node.children:
                    nex += [node.children[letter]]
            cur, nex = nex, []
        for node in cur:
            if node.isEnd:
                return True
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)