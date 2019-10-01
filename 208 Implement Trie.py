#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 15:59:05 2019

@author: alberthsu
"""

"""
208. Implement Trie (Prefix Tree)
Implement a trie with insert, search, and startsWith methods.
"""

import collections

class TrieNode:
    
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for char in word:
            node = node.children[char]
        node.isWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for char in word:
            node = node.children.get(char)
            if not node: return False
        return node.isWord

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for char in prefix:
            node = node.children.get(char)
            if not node: return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
