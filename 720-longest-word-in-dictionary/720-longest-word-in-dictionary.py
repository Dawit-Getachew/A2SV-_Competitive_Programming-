class TrieNode:
    def __init__(self):
        self.children = {}

class Solution:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word):
        curr = self.root
        count= 0
        if len(word) > 1 and word[0] not in curr.children:
            return
        for i in range(len(word)):
            if word[i] not in curr.children:
                if len(word[i:]) > 1: break
                curr.children[word[i]] = TrieNode()
            curr = curr.children[word[i]]
            
    def search(self, word):
        curr = self.root
        for char in list(word):
            if char in curr.children:
                curr = curr.children[char]
            else:
                return False
        return True
    
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        print(words)
        for word in words:
            self.insert(word)
        ans = ""
        for word in words:
            if self.search(word) and (len(word) > len(ans) or ( len(word) == len(ans) and word < ans)):
                ans = word
        return ans
        