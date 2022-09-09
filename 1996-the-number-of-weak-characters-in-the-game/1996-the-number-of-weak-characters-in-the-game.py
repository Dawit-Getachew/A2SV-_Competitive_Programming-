class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        maxAttack = max(a for a, _ in properties)
        maxDefense = [0] * (maxAttack+2)
        
        for a, b in properties:
            maxDefense[a] = max(maxDefense[a], b)
        
        for i in reversed(range(len(maxDefense)-1)):
            maxDefense[i] = max(maxDefense[i], maxDefense[i+1])
        
        ans = 0
        for a, b in properties:
            if b < maxDefense[a+1]:
                ans += 1
        return ans
    