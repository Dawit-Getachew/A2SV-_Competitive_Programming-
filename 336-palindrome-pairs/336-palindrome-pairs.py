class Trie:
    def __init__(self):
        self._root = {}
    
    def add(self, word, index):
        _iter = self._root
        for char in word:
            if char not in _iter:
                _iter[char] = {}
            _iter = _iter[char]
        _iter["*"] = index
    
    def _dfs_to_leaf(self, trie_node):
        stack = [trie_node]
        result = []
        while stack:
            trie_node = stack.pop()
            for char in trie_node:
                if char == "*":
                    result.append(trie_node[char])
                else:
                    stack.append(trie_node[char])
        return result
                
    def search_indexes(self, word):
        _iter = self._root
        for char in word:
            if char not in _iter:
                return []
            _iter = _iter[char]
        return self._dfs_to_leaf(_iter)

class Solution:
    def is_palindrome(self, word, start, end):
        while start < end:
            if word[start] == word[end]:
                start += 1
                end -= 1
            else:
                return False
        return True
    
    def find_self_palindromes(self, words, skip_index=None):
        result = []

        for i, w in enumerate(words):
            if i == skip_index:
                continue

            if self.is_palindrome(w, 0, len(w)-1):
                result.append(i)
        
        return result
    
    def find_suffix_palindromes(self, words):
        suffix_trie = Trie()
        result = []
        for i, word in enumerate(words):
            if word != "":
                suffix_trie.add(word[::-1], i)
        
        for i, word in enumerate(words):
            suffix_word_indexes = suffix_trie.search_indexes(word)
            for suffix_word_index in suffix_word_indexes:
                if i == suffix_word_index:
                    continue

                probable_word = words[suffix_word_index]
                start_index = 0
                end_index = len(words[suffix_word_index])-len(word)-1
                if self.is_palindrome(probable_word, start_index, end_index):
                    result.append((i, suffix_word_index))

        return result
    
    def find_prefix_palindromes(self, words):
        prefix_trie = Trie()
        result = []
        for i, word in enumerate(words):
            if word != "":
                prefix_trie.add(word, i)

        for i, word in enumerate(words):
            prefix_word_indexes = prefix_trie.search_indexes(word[::-1])
            for prefix_word_index in prefix_word_indexes:
                if i == prefix_word_index:
                    continue

                probable_word = words[prefix_word_index]
                start_index = len(word)
                end_index = len(probable_word)-1
                if self.is_palindrome(probable_word, start_index, end_index):
                    result.append((prefix_word_index, i))

        return result

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        result = set()
            
        for i, word in enumerate(words):
            if word == "":
                result.update([(i, j) for j in self.find_self_palindromes(words, skip_index=i)])

        result.update(self.find_suffix_palindromes(words))
        result.update(self.find_prefix_palindromes(words))
        
        return result  