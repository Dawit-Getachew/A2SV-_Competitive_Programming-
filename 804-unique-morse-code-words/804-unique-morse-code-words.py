class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        res = set()
        charMap = {}
        morseCode = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        a = list(string.ascii_lowercase)
        for i in range(len(morseCode)):
            charMap[a[i]] = morseCode[i]
        for word in words:
            morseWord = ""
            for char in word:
                morseWord += charMap[char]
            res.add(morseWord)
        return len(res)