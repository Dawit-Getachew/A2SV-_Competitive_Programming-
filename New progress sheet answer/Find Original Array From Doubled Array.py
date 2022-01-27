class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 == 1:
            return []
        
        changed.sort()
        doubles = defaultdict(int)
        result = []
        for i in range(len(changed)):
            if doubles[changed[i]] > 0 :
                result.append(changed[i] // 2)
                doubles[changed[i]] -= 1
            else:
                doubles[changed[i]*2] += 1
        
        return result if len(result) == len(changed) // 2 else []