class Solution:            
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        sentence =  sentence.split()
        for word in dictionary:
            for i in range(len(sentence)):
                if word[0] != sentence[i][0]:
                    continue
                if len(sentence) >= len(word) and word == sentence[i][:len(word)]:
                    sentence[i] = word
        return ' '.join(sentence)