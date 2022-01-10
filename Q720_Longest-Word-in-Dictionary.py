from collections import deque
class Solution:
    def longestWord(self, words: List[str]) -> str:
        class Trie_node:
            def __init__(self):
                self.children = collections.defaultdict(Trie_node)
                self.is_end = False
                self.word = ""
        class Trie:
            def __init__(self):
                self.root = Trie_node()
            
            def insert(self, word):
                node = self.root
                
                for letter in word:
                    node = node.children[letter]
                node.is_end = True
                node.word = word
            
            def search_largest(self):
                longest_word = ""
                queue = deque([self.root])
                
                while queue:
                    node = queue.popleft()
                    for child_node in node.children.values():
                        if child_node.is_end:
                            queue.append(child_node)
                            if len(child_node.word) > len(longest_word):
                                longest_word = child_node.word
                return longest_word
        trie = Trie()
        words.sort()
        for word in words:
            trie.insert(word)
        return trie.search_largest()
            