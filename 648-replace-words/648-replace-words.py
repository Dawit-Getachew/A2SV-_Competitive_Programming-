class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Solution:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.isWord = True
        
    def search(self, sent):
        curr = self.root
        lis = []
        flag = False
        for char in sent:
            if char in curr.children:
                curr = curr.children[char]
                lis.append(char)
                if curr.isWord == True:
                    return ''.join(lis)
            else: return False
            
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        for word in dictionary:
            self.insert(word)
        sentence = sentence.split()
        for i in range(len(sentence)):
            res = self.search(sentence[i])
            if res:
                sentence[i] = res
        return ' '.join(sentence)