"""
!1032. Stream of Characters
Implement the StreamChecker class as follows:
•	StreamChecker(words): Constructor, init the data structure with the given words.
•	query(letter): returns true if and only if for some k >= 1, the last k characters queried (in order from oldest to newest, including this letter just queried) spell one of the words in the given list.
"""

#Trie

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True

class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.letters = []
        for word in words:
            self.trie.insert(word[::-1])


    def query(self, letter: str) -> bool:
        self.letters.append(letter)
        k = len(self.letters)-1
        node = self.trie.root
        while k >= 0:
            if node.isWord: return True
            if self.letters[k] not in node.children: return False
            node = node.children[self.letters[k]]
            k -= 1
        return node.isWord
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
