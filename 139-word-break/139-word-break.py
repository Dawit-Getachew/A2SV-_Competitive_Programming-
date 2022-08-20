class Trie:
    def __init__(self):
        self.nodes= collections.defaultdict(Trie)
        self.isWord= False
        
    def addWord(self,word):
        current= self
        for c in word:
            current= current.nodes[c]    
        current.isWord= True
        

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root= Trie()
        for word in wordDict:
            root.addWord(word)
        
        tries= set([root])
        for c in s:
            tries= {trie.nodes[c] for trie in tries if c in trie.nodes} 
            if any(trie.isWord for trie in tries):
                tries.add(root)
        return any(trie.isWord for trie in tries)