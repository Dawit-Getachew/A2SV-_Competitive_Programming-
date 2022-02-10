class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        guess = list(guess)
        secret = list(secret)
        counter = collections.Counter(secret)
        aCounts, bCounts = 0, 0
        
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                counter[secret[i]] -= 1
                guess[i] = 'A'
                secret[i] = 'A'
                aCounts += 1
                
        
        for i in range(len(guess)):
            if guess[i] != 'A' and counter[guess[i]] > 0:
                counter[guess[i]] -= 1
                guess[i] = 'B'
                bCounts += 1
                
        return str(aCounts) + 'A'+ str(bCounts) + 'B'