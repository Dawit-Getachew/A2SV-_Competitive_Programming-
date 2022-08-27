class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        if len(words)==1:
            return words
        
        repeat = True
        while repeat:
            i=1
            repeat=False
            while i<len(words):
                if sorted(words[i])==sorted(words[i-1]):
                    words.pop(i)
                    i-=1
                    repeat=True
                i+=1
        return words