"""
1268. Search Suggestions System
Given an array of strings products and a string searchWord. We want to design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with the searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.
Return list of lists of the suggested products after each character of searchWord is typed. 
"""

#Trie

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.words = []
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
            node.words.append(word)
            node.words.sort()
            if len(node.words) > 3: node.words.pop()
        node.isWord = True

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        res = []
        trie = Trie()
        node = trie.root
        for product in products: trie.insert(product)
        for w in searchWord:
            node = node.children.get(w)
            if not node: break
            res.append(node.words)
        remain = len(searchWord)-len(res)
        for i in range(remain): res.append([])
        return res
