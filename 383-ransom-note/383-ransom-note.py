class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashRan = defaultdict(int)
        hashMag = defaultdict(int)
        for i in ransomNote:
            hashRan[i] += 1
        for i in magazine:
            hashMag[i] += 1
        for i in hashRan:
            if hashMag[i] >= hashRan[i]:
                continue
            else:
                return False
        return True