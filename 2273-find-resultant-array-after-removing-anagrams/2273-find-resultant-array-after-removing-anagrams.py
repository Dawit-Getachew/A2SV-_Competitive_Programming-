class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        i=1
        while(i<len(words)):
            e1=sorted(words[i-1])
            e2=sorted(words[i])
            if e1==e2:
                words.pop(i)
            else:
                i=i+1
        return words