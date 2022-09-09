class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        maxAttackValue = 0
        minAttackValue = float("inf")
        maxDefense = [0] * 100002
        
        for p in properties:
            maxDefense[p[0]] = max(maxDefense[p[0]], p[1])
            minAttackValue = min(minAttackValue, p[0])
            maxAttackValue = max(maxAttackValue, p[0])
        
        maxDefenseValue = 0
        
        for i in range(maxAttackValue, minAttackValue - 1, -1):
            if maxDefenseValue > maxDefense[i]:
                maxDefense[i] = maxDefenseValue
            else:
                maxDefenseValue = maxDefense[i]
        
        res = 0
        
        for p in properties:
            if maxDefense[p[0] + 1] > p[1]:
                res += 1
        return res