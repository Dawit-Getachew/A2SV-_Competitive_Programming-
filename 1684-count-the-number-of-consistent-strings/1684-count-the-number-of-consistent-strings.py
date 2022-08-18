class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        allowed = set(allowed)
        for word in words:
            for i in word:
                if i in allowed:
                    continue
                else:
                    count -= 1
                    break
            count+=1
        return count